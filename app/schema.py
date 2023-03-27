from typing import Any, Dict, Optional, Type

from errors import ApiError
from pydantic import BaseModel, ValidationError


class CreateAd(BaseModel):

    description: str
    owner: str

class PatchAd(BaseModel):

    description: Optional[str]
    owner: Optional[str]

SCHEMA_TYPE = Type[CreateAd] | Type[PatchAd]


def validate(schema: SCHEMA_TYPE, data: Dict[str, Any], exclude_none: bool = True) -> dict:
    try:
        validated = schema(**data).dict(exclude_none=exclude_none)
    except ValidationError as er:
        raise ApiError(400, er.errors())
    return validated