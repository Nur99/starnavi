from datetime import timedelta

import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils import timezone

from apps.users.models import CustomUser
from apps.users.utils.constants import (
    ACCESS_TOKEN_EXPIRATION,
    REFRESH_TOKEN_EXPIRATION,
    JWTAlgorithm,
)
from apps.users.utils.exceptions import CustomException


def generate_token(user, token_expiration):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "iat": timezone.now(),
        "exp": timezone.now() + timedelta(minutes=token_expiration),
    }
    token = jwt.encode(
        payload, settings.TOKEN_SECRET_KEY, algorithm=JWTAlgorithm.HS256.value
    )
    return token


def generate_tokens(user):
    access_token = generate_token(user, ACCESS_TOKEN_EXPIRATION)
    refresh_token = generate_token(user, REFRESH_TOKEN_EXPIRATION)
    tokens = {"access_token": access_token, "refresh_token": refresh_token}

    return user, tokens


def create_user(email, username, password):
    user = CustomUser(
        email=email,
        username=username,
    )
    user.set_password(password)
    user.save()

    return generate_tokens(user)


def login_user(username, password):
    user = authenticate(username=username, password=password)
    if not user:
        raise CustomException()

    CustomUser.objects.filter(username=username).update(last_login=timezone.now())

    return generate_tokens(user)
