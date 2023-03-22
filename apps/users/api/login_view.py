from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.services.user_actions import login_user


class UserLoginView(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

        class Meta:
            ref_name = "UserLoginViewInputSerializer"

    @extend_schema(request=InputSerializer, responses=None)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(login_user(**serializer.validated_data))
