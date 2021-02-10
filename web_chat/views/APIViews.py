from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from web_chat.models import Chat, Message
from web_chat.serializers import ChatSerializer, MessageSerializer


class ChatListAPI(APIView):
    """
    List all chats, or create a new chat.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        chats = Chat.objects.all().filter(members=request.user)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatSerializer(data=request.data)

        if serializer.is_valid() and len(serializer.validated_data['members']) == 2 and request.user in \
                serializer.validated_data['members']:

            if Chat.objects.filter(members=serializer.validated_data['members'][0]).filter(
                    members=serializer.validated_data['members'][1]).count() == 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                existing_chat = Chat.objects.filter(members=serializer.validated_data['members'][0]).filter(
                    members=serializer.validated_data['members'][1]).first()

                return Response({"id": existing_chat.id}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatDetailAPI(APIView):
    """
    Retrieve, update or delete a chat instance.
    """

    def get_object(self, pk):
        try:
            return Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chat = self.get_object(pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)


class ChatMessagesAPI(APIView):
    """
    List all messages, or create a new message.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user_id):
        try:
            # check if user has access to selected chat
            chat = Chat.objects.filter(members__in=[user_id]).get(pk=pk)
            return chat
        except Chat.DoesNotExist:
            raise Http404

    # get messages from chat
    def get(self, request, pk, format=None):
        chat = self.get_object(pk, request.user.id)
        messages = Message.objects.filter(chat_id=chat.id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    # send message
    def post(self, request, pk, format=None):
        chat = self.get_object(pk, request.user.id)
        request.data.update({"author_id": request.user.id, "chat_id": chat.id})
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
