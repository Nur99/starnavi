from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import CustomUser
from apps.users.services.user_actions import create_user


class UserSignupView(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ("username", "email", "password")
            ref_name = "UserSignupViewInputSerializer"

    @extend_schema(request=InputSerializer, responses=None)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(create_user(**serializer.validated_data))
