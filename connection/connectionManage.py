from fastapi                import WebSocket
from models.entity.actions  import Action
from models.entity.user     import User
from models.entity.letter   import Letter
from models.entity.player   import Player
from pydantic               import BaseModel
from typing                 import Optional
from models.entity.letter import Letter
from models.entity.actions import Action

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
    [Letter(id=2, name='capitao', hide=True, actions=[
        (Action.BLOCKTOSTEAL.name, Action.BLOCKTOSTEAL.value),
        (Action.BLOCKTOSTEAL.name, Action.TOSTEAL.value)
    ]) for _ in range(amount)] +
    [Letter(id=1, name='assassino', hide=True, actions=[
        (Action.KILLER.name, Action.KILLER.value)
    ]) for _ in range(amount)] +
    [Letter(id=3, name='condensa', hide=True, actions=[
        (Action.BLOCKKILLER.name, Action.BLOCKKILLER.value)
    ]) for _ in range(amount)] +
    [Letter(id=4, name='duque', hide=True, actions=[
        (Action.BLOCKBUY3COINS.name, Action.BLOCKBUY3COINS.value),
        (Action.BUY3COINS.name, Action.BUY3COINS.value),
        (Action.BLOCKEXHELP.name, Action.BLOCKEXHELP.value)
    ]) for _ in range(amount)] +
    [Letter(id=5, name='embaixador', hide=True, actions=[
        (Action.BLOCKTOSTEAL.name, Action.BLOCKTOSTEAL.value),
        (Action.CHANGELETTERS.name, Action.CHANGELETTERS.value)
    ]) for _ in range(amount)]
]

    
    return cartas


class ConnectionManager:

    def __init__(self):
        self.historic:list[str] = []
        self.users:list[User] = []
        self.userAction = 0
        self.userReaction = 1
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

    