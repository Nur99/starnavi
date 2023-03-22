from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework.authentication import BaseAuthentication

from apps.users.models import CustomUser
from apps.users.utils import codes, messages


class JWTAuthentication(BaseAuthentication):
    """
    Custom authentication class for DRF and JWT.
    """

    def authenticate(self, request):
        from .exceptions import CustomException
        from .token import decode_token

        header = request.META.get("HTTP_AUTHORIZATION")

        if not header:
            return None
        # header = 'Bearer xxxxxxxxxxxxxxxxxxxxxxxx'
        prefix = header.split(" ")[0]
        if prefix != "Bearer":
            raise CustomException(
                code=codes.AUTHENTICATION_ERROR,
                detail=messages.TOKEN_PREFIX_INVALID,
            )
        access_token = header.split(" ")[1]
        payload = decode_token(token=access_token)

        user = CustomUser(payload["user_id"], payload["username"])

        return (user, None)


class SwaggerAuthentication(OpenApiAuthenticationExtension):
    target_class = "apps.users.utils.authentication.JWTAuthentication"
    name = "JWTAuthentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Value should be formatted: `<key>`. Without prefix",
        }
