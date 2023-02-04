import datetime

from django.contrib.auth.models import User
from django.db import models


class UserChat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_status = models.CharField(max_length=20)


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_text = models.CharField(max_length=1000)
    message_time = models.DateTimeField(default=datetime.datetime.now())
    message_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_from")
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_to")
    message_chat = models.ForeignKey(UserChat, on_delete=models.CASCADE)


class SingleChatBox:
    from_user = User()
    to_user = User()
    sorted_messages = []

    def __init__(self, from_user=None, to_user=None, messages=[]):
        self.from_user = from_user
        self.to_user = to_user
        self.sorted_messages = sorted(messages, key=lambda msg: msg.message_time)
