from pydantic import BaseModel
from models.entity.letter import Letter


class PlayerScheme(BaseModel):
    id:int
    name:str
    coins:int
    letters:list[dict]