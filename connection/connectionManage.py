from fastapi                import WebSocket
from models.entity.actions  import Action
from models.entity.user     import User
from pydantic               import BaseModel
from typing                 import Optional

class SendAction(BaseModel):
    action:Action
    userSend:User
    userReceives:Optional[User] = None

    def toString(self) -> str:
        return f'{self.userSend.name} fez ação {self.action.name} a {self.userReceives.name if self.userReceives != None else "Mesa"} '
    ...


class ConnectionManager:

    def __init__(self):
        self.historic:list[str] = []
        self.users:list[User] = []
        self.userAction = 0
        self.game = False
        pass


    async def connect(self, id:int,name:str ,websocket:WebSocket):
        if(not self.game):
            await websocket.accept()
            self.users.append(User(id=id,name=name, webSocket=websocket))
        return {'message':'Jogo em andamento'}
        ...

    
    async def ready(self):
        for user in self.users:
            await user.webSocket.send_json({'id':self.userAction})


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
        {
           await websocket.send_json(body)
        }


    async def broadcast(self):
        for user in self.users:
            await user.webSocket.send_json(self.historic)
        ...




manager = ConnectionManager()

    