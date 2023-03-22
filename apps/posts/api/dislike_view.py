from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.services.post_actions import dislike_post


class DislikeView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(request=None, responses=None)
    def post(self, request, post_id):
        dislike_post(user=self.request.user, post_id=post_id)

        return Response(status=200)
