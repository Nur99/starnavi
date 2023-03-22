from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.models import Post
from apps.posts.services.post_actions import create_post


class CreatePostView(APIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ("title", "text")
            ref_name = "CreatePostViewInputSerializer"

    permission_classes = (IsAuthenticated,)

    @extend_schema(request=InputSerializer, responses=None)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_post(user=self.request.user, **serializer.validated_data)

        return Response(status=201)
