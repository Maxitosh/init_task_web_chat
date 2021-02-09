from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chat


# class MembersSerializer(serializers.Serializer):
#     class Meta:
#         model = User


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Chat
        fields = ['id', 'members']
