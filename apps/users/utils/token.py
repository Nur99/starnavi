from typing import Any, Dict

import jwt
from django.conf import settings

from . import codes, messages
from .constants import JWTAlgorithm
from .exceptions import CustomException


def decode_token(*, token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(
            token,
            settings.TOKEN_SECRET_KEY,
            algorithms=JWTAlgorithm.list(),
        )
    except jwt.ExpiredSignatureError:
        raise CustomException(
            code=codes.AUTHENTICATION_ERROR, detail=messages.TOKEN_EXPIRED
        )
    except (jwt.InvalidSignatureError, jwt.exceptions.DecodeError):  # type: ignore
        raise CustomException(
            code=codes.AUTHENTICATION_ERROR, detail=messages.TOKEN_INVALID
        )
    except ValueError:
        try:
            payload = jwt.decode(
                token,
                settings.TOKEN_PUBLIC_KEY,
                algorithms=JWTAlgorithm.list(),
            )
        except jwt.ExpiredSignatureError:
            raise CustomException(
                code=codes.AUTHENTICATION_ERROR, detail=messages.TOKEN_EXPIRED
            )
        except (jwt.InvalidSignatureError, jwt.exceptions.DecodeError, ValueError):  # type: ignore
            raise CustomException(
                code=codes.AUTHENTICATION_ERROR, detail=messages.TOKEN_INVALID
            )
    return payload
