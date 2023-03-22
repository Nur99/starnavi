from django.db import models
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser
from apps.utils import constants


class Post(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} / f{self.author}"


class Like(models.Model):
    created = models.DateField(default=now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"like: {self.author} / f{self.created}"

    def clean(self):
        if (
            Like.objects.filter(post_id=self.post_id, author_id=self.author_id).count()
            == constants.MAX_LIKE_PER_USER
        ):
            raise ValidationError(
                detail=f"You cannot like more than {constants.MAX_LIKE_PER_USER} times"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Like, self).save(*args, **kwargs)


class DisLike(Like):
    def __str__(self):
        return f"dislike: {self.author} / f{self.created}"

    def clean(self):
        if (
            DisLike.objects.filter(
                post_id=self.post_id, author_id=self.author_id
            ).count()
            == constants.MAX_DISLIKE_PER_USER
        ):
            raise ValidationError(
                detail=f"You cannot dislike more than {constants.MAX_DISLIKE_PER_USER} times"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(DisLike, self).save(*args, **kwargs)
