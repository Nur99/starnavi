import os
import random
import sys
from typing import List

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
fake = Faker()

from apps.posts.models import Like, Post  # noqa
from apps.users.models import CustomUser  # noqa
from apps.utils import constants  # noqa


def number_of_users():
    return len(CustomUser.objects.all())


def max_posts_per_user():
    return constants.MAX_POST_PER_USER


def max_likes_per_user():
    return constants.MAX_LIKE_PER_USER


def signup_users(parameters: List[str]):
    user_amount = int(parameters[2])

    users = []
    usernames = []
    for i in range(user_amount):
        username = fake.name()
        usernames.append(username)
        user = CustomUser(email=fake.email(), username=username, password=fake.name())
        users.append(user)

    CustomUser.objects.bulk_create(
        objs=users,
    )

    created_users = CustomUser.objects.filter(username__in=usernames)

    posts = []
    post_titles = []
    for user in created_users:
        post_number = random.randint(0, constants.MAX_POST_PER_USER)
        for i in range(post_number):
            post_name = fake.name()
            post_titles.append(post_name)
            user_posts = [
                Post(title=post_name, text=fake.text(), author_id=user.id)
                for i in range(post_number)
            ]
            posts = posts + user_posts

    Post.objects.bulk_create(objs=posts)

    created_posts = Post.objects.filter(title__in=post_titles)

    likes = []
    for post in created_posts:
        for user in created_users:
            max_like = random.randint(0, constants.MAX_LIKE_PER_USER)
            for i in range(max_like):
                likes.append(Like(post_id=post.id, author_id=user.id))

    Like.objects.bulk_create(objs=likes)


config_methods = {
    "number_of_users": number_of_users,
    "max_posts_per_user": max_posts_per_user,
    "max_likes_per_user": max_likes_per_user,
    "signup_users": signup_users,
}


def main():
    config = sys.argv[1]
    if config_methods.get(config):
        if len(sys.argv) > 2:
            print(config_methods[config](parameters=sys.argv))
        else:
            print(config_methods[config]())
    else:
        print(f"{config} command is not found")


if __name__ == "__main__":
    main()
