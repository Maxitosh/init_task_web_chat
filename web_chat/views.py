from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from web_chat.forms import MessageForm
from web_chat.models import Chat
from web_chat.serializers import ChatSerializer


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'


class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'chat_list.html', {'user_profile': request.user, 'chats': chats})


class ChatListAPI(APIView):
    """
    List all chats, or create a new chat.
    """

    def get(self, request, format=None):
        chats = Chat.objects.all().filter(members=request.user)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ChatSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ChatSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_read=False).exclude(author=request.user).update(is_read=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            'messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messages', kwargs={'chat_id': chat_id}))


class CreateDialogView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        print(f"users:{request.user.id} and {user_id}")
        chats = Chat.objects.filter(members__in=[request.user.id]).filter(members__in=[user_id])
        print(chats)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('messages', kwargs={'chat_id': chat.id}))


class CreateChatView(LoginRequiredMixin, CreateView):  # new
    model = Chat
    template_name = 'create_chat.html'
    fields = ('members',)

    def form_valid(self, form):  # new
        print(form.data)
        form.instance.user = self.request.user
        return redirect(reverse('create_dialog', kwargs={'user_id': int(form.data['members'][0])}))

    def get_form(self, form_class=None):
        form = super(CreateChatView, self).get_form(form_class)
        form.fields['members'].queryset = User.objects.exclude(id=self.request.user.id)
        return form
