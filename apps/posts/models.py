from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.utils import constants


class Post(models.Model):
    title = models.CharField(max_length=1000, verbose_name=_("title"))
    text = models.TextField(verbose_name=_("text"))
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name="author",
        related_name="posts",
    )

    def __str__(self):
        return f"{self.title} / f{self.author}"

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Like(models.Model):
    class LikeType(models.TextChoices):
        LIKE = "LIKE", "Like"
        DISLIKE = "DISLIKE", "Dislike"

    created = models.DateField(default=now, verbose_name=_("created"))
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, verbose_name=_("post"), related_name="posts"
    )
    author = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        verbose_name=_("author"),
        related_name="likes",
    )
    like_type = models.CharField(
        max_length=15,
        choices=LikeType.choices,
        default=LikeType.LIKE,
        verbose_name=_("like type"),
    )

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def clean(self):
        if (
            Like.objects.filter(
                post_id=self.post_id,
                author_id=self.author_id,
                like_type=Like.LikeType.LIKE,
            ).count()
            == constants.MAX_LIKE_PER_USER
        ):
            raise ValidationError(
                detail=f"You cannot like more than {constants.MAX_LIKE_PER_USER} times"
            )
        if (
            Like.objects.filter(
                post_id=self.post_id,
                author_id=self.author_id,
                like_type=Like.LikeType.DISLIKE,
            ).count()
            == constants.MAX_DISLIKE_PER_USER
        ):
            raise ValidationError(
                detail=f"You cannot dislike more than {constants.MAX_DISLIKE_PER_USER} times"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Like, self).save(*args, **kwargs)

    def __str__(self):
        return f"like: {self.author} / f{self.created}"
