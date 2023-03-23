from django.db.models import Count

from apps.posts.models import Like, Post


def create_post(user, title, text):
    Post.objects.create(author=user, title=title, text=text)


def like_post(user, post_id, like_type):
    Like.objects.create(author=user, post_id=post_id, like_type=like_type)


def get_analytics(date_from, date_to):
    likes = Like.objects.all()
    if date_from:
        likes = likes.filter(created__gte=date_from)
    if date_to:
        likes = likes.filter(created__lte=date_to)

    return likes.values("created").annotate(likes=Count("id"))
