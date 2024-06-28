from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, UUID4, Field



class BaseSchema(BaseModel):
    class config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field('Data de criação')]