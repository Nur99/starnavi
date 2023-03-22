from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.posts.services.post_actions import get_analytics


class AnalyticsView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="date_from",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="date_to",
                required=False,
                type=str,
            ),
        ],
        request=None,
        responses=None,
    )
    def get(self, request):
        date_from = self.request.query_params.get("date_from", None)
        date_to = self.request.query_params.get("date_to", None)

        data = get_analytics(date_from, date_to)

        return Response(data=data, status=200)
