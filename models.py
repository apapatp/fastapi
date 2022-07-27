from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

from pydantic.class_validators import List


class Role(str, Enum):
    admin = "admin"
    general = "general"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    roles: List[Role]


class Transaction(BaseModel):
    transaction_id: Optional[UUID] = uuid4()
    user: Optional[User]