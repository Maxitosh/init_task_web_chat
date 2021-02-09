from django import forms
from django.forms import ModelForm

from web_chat.models import Message, Chat


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}


