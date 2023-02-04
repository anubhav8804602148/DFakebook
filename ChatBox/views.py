from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ChatBox.models import Message
from util.Logger import Logger

CHAT_PAGE = "chat_page.html"
logger = Logger("fakebook.log")


def show_chat_home(request):
    logger.log_request(request)
    if not request.user.is_authenticated:
        return redirect("/login")
    current_user = request.user
    all_messages_from_user = Message.objects.filter(message_from=request.user)
    all_messages_to_user = Message.objects.filter(message_to=request.user)
    all_messages = list(all_messages_from_user)+list(all_messages_to_user)
    all_users_involved = set(
        list(map(lambda msg: msg.message_to, all_messages)) +
        list(map(lambda msg: msg.message_from, all_messages))
    )
    all_messages_mapped = {}
    for usr in all_users_involved:
        all_messages_mapped[usr] = []
    for message in all_messages:
        if message.message_from == current_user:
            all_messages_mapped[message.message_to] += [message]
        elif message.message_to == current_user:
            all_messages_mapped[message.message_from] += [message]
    logger.log(all_messages_mapped)
    return render(request, template_name=CHAT_PAGE, context={
        "user": request.user,
        "all_users_involved": all_users_involved,
        "all_users": User.objects.all(),
        "all_messages": all_messages_mapped
    })
