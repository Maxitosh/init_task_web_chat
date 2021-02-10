from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User)

    def get_absolute_url(self):
        return f"dialogs/{self.pk}"
