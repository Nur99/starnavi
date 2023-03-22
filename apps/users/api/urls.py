from django.urls import path

from .login_view import UserLoginView
from .signup_view import UserSignupView

urlpatterns = [
    path("signup/", UserSignupView.as_view()),
    path("login/", UserLoginView.as_view()),
]
