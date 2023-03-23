from django.urls import path

from apps.posts.api.analytics_view import AnalyticsView
from apps.posts.api.create_post_view import CreatePostView
from apps.posts.api.like_view import LikeView

urlpatterns = [
    path("posts/create", CreatePostView.as_view()),
    path("posts/<int:post_id>/like", LikeView.as_view()),
    path("analytics/", AnalyticsView.as_view()),
]
