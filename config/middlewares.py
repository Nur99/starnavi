from django.utils import timezone

from apps.users.models import CustomUser


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.user:
            return response

        user: CustomUser = request.user
        if user.is_authenticated:
            CustomUser.objects.filter(id=request.user.id).update(
                last_login=timezone.now()
            )
        return response
