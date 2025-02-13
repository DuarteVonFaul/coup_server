from fastapi                import WebSocket
from models.entity.actions  import Action
from models.entity.user     import User
from models.entity.letter   import Letter
from models.entity.player   import Player
from pydantic               import BaseModel
from typing                 import Optional
from models.entity.letter import Letter
from models.entity.actions import BlockAction, PrimaryAction, ProtectiveAction

import random


class SendAction(BaseModel):
    action:Action
    userSend:User
    userReceives:Optional[User] = None

    def toString(self) -> str:
        return f'{self.userSend.name} fez ação {self.action.name} a {self.userReceives.name if self.userReceives != None else "Mesa"} '
    ...


def letters(amount):
    cartas = [
    [Letter(id=2, name='capitao', hide=False, actions=[
        (ProtectiveAction.BLOCKTOSTEAL.name, ProtectiveAction.BLOCKTOSTEAL.value),
        (ProtectiveAction.BLOCKTOSTEAL.name, PrimaryAction.TOSTEAL.value)
    ]) for _ in range(amount)] +
    [Letter(id=1, name='assassino', hide=False, actions=[
        (PrimaryAction.KILLER.name, PrimaryAction.KILLER.value)
    ]) for _ in range(amount)] +
    [Letter(id=3, name='condensa', hide=False, actions=[
        (ProtectiveAction.BLOCKKILLER.name, ProtectiveAction.BLOCKKILLER.value)
    ]) for _ in range(amount)] +
    [Letter(id=4, name='duque', hide=False, actions=[
        (BlockAction.BLOCKBUY3COINS.name, BlockAction.BLOCKBUY3COINS.value),
        (PrimaryAction.BUY3COINS.name, PrimaryAction.BUY3COINS.value),
        (BlockAction.BLOCKEXHELP.name, BlockAction.BLOCKEXHELP.value)
    ]) for _ in range(amount)] +
    [Letter(id=5, name='embaixador', hide=False, actions=[
        (ProtectiveAction.BLOCKTOSTEAL.name, ProtectiveAction.BLOCKTOSTEAL.value),
        (PrimaryAction.CHANGELETTERS.name, PrimaryAction.CHANGELETTERS.value)
    ]) for _ in range(amount)]
]

    
    return cartas


class ConnectionManager:

    def __init__(self):
        self.historic:list[str] = []
        self.users:list[User] = []
        self.userAction = 0
        self.game = False
        self.letters:list[Letter] = []
        pass


    async def connect(self, id:int,name:str ,websocket:WebSocket):
        if(not self.game and len(self.users) < 8):
            
            await websocket.accept()
            self.users.append(User(id=id,name=name, webSocket=websocket))
        return {'message':'Jogo em andamento'}
        ...

    
    def ready(self):
        amount = len(self.users)
        if amount <= 4 : 
            self.letters = letters(3)[0]
        elif amount <= 6:
            self.letters = letters(4)[0]
        else:
            self.letters = letters(6)[0]

        

        for user in self.users:
            random.shuffle(self.letters)
            user.player = Player(coins=2,Letters=[self.letters.pop(), self.letters.pop()])
        
            


    def disconnect(self, websocket:WebSocket):
        for user in self.users:
            if(user.webSocket == websocket):
                self.users.remove(user)
        ...

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
        self.historic.append(message)

    async def send_action(self, action:SendAction):
        if action.userReceives != None:
            await action.userReceives.webSocket.send_json(action)
            self.historic.append(action.toString())
            self.send_historic()
        else:
            for user in self.users:
                await user.webSocket.send_json(action)
            self.historic.append(action.toString())
            self.send_historic()
        ...

    async def send_command(self, body, websocket: WebSocket):
        await websocket.send_json(body)
        


    async def broadcast(self):
        for user in self.users:
            await user.webSocket.send_json(self.historic)
        ...




manager = ConnectionManager()

    