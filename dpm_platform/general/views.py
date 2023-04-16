from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


class BellView(GenericAPIView):
    @extend_schema(
        tags=['account'],
        parameters=[],
        responses={},
        operation_id='get_bell',
    )
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:

        return Response()
