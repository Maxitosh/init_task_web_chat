from rest_framework import serializers

from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Chat
        fields = ['id', 'members']


class MessageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    message = serializers.CharField()
    author_id = serializers.IntegerField()
    chat_id = serializers.IntegerField()

    class Meta:
        model = Message
        fields = ['id', 'message', 'pub_date', 'is_read', 'author_id', 'chat_id']
