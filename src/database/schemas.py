from datetime import datetime

from pydantic import BaseModel, ConfigDict
from .models import WeightType, MachineCategory


class UserPydantic(BaseModel):
    id: int
    user_id: int
    chat_id: int

    model_config = ConfigDict(from_attributes=True)


class MachinePydantic(BaseModel):
    name: str
    category: MachineCategory
    weight_type: WeightType
    pic_path: str | None
    user: UserPydantic

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
