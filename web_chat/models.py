from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User)

    def get_absolute_url(self):
        return f"dialogs/{self.pk}"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.DO_NOTHING)
    message = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
