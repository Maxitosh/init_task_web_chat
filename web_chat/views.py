from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from web_chat.models import Chat
from web_chat.serializers import ChatSerializer


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'


@api_view(['GET', 'POST'])
def chats_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def chat_details(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        chat = Chat.objects.get(pk=pk)
    except Chat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return JsonResponse(serializer.data)
