# Generated by Django 3.2.9 on 2023-03-23 07:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="created"
                    ),
                ),
                (
                    "like_type",
                    models.CharField(
                        choices=[("LIKE", "Like"), ("DISLIKE", "Dislike")],
                        default="LIKE",
                        max_length=15,
                        verbose_name="like type",
                    ),
                ),
            ],
            options={
                "verbose_name": "Like",
                "verbose_name_plural": "Likes",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1000, verbose_name="title")),
                ("text", models.TextField(verbose_name="text")),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
