from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.models import Like
from apps.posts.services.post_actions import like_post


class LikeView(APIView):
    permission_classes = (IsAuthenticated,)

    class InputSerializer(serializers.Serializer):
        like_type = serializers.ChoiceField(choices=Like.LikeType.choices)

    @extend_schema(request=InputSerializer, responses=None)
    def post(self, request, post_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_post(
            user=self.request.user,
            post_id=post_id,
            like_type=serializer.validated_data["like_type"],
        )

        return Response(status=200)
