from models.entity.actions import Action
from pydantic import BaseModel


class Letter(BaseModel):

    id:int
    name:str
    image:str
    hide:bool
    actions:list[Action]