import logging
import traceback

from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.serializers import as_serializer_error
from rest_framework.views import exception_handler

from .codes import BAD_REQUEST

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    APIException:
        {
            "code": 1
            "message": "Error message"
        }

    DRF ValidationError:
        {
            "code": 1
            "message": "Validation error"
            "fields": {}
        }

    CustomException:
        {
            "code": 1
            "message": "Application error"
        }
    """
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, context)

    logger.warning(
        "".join(traceback.format_exception(None, value=exc, tb=exc.__traceback__))
    )
    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    if isinstance(exc.detail, (list, dict)):
        response.data = {"detail": response.data}

    if isinstance(exc, exceptions.ValidationError):
        response.data["message"] = "Validation error"
        response.data["fields"] = response.data["detail"]
    else:
        response.data["message"] = response.data["detail"]

    response.data["code"] = exc.get_codes()
    if type(response.data["code"]) != int:
        response.data["code"] = BAD_REQUEST

    del response.data["detail"]
    return response


class CustomException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Custom exception"
    default_code = BAD_REQUEST
