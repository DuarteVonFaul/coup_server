from models.entity.letter import Letter
from pydantic import BaseModel


class Player(BaseModel):

    coins:int
    Letters:list[Letter]