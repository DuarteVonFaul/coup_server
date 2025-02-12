from fastapi import WebSocket
from pydantic import BaseModel
from models.entity.player import Player
from typing                 import Optional

class User(BaseModel):

    id:int
    webSocket:WebSocket
    name:str
    player:Optional[Player] = None

    model_config = {
        "arbitrary_types_allowed": True  # Permite tipos arbitrários
    }