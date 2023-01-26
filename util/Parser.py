from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def request_data_to_user(post_data):
    user = User()
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    user.password = make_password(post_data.get('password'))
    return user

