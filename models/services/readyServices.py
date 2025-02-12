from connection.connectionManage import ConnectionManager
from models.schemas.userPublic   import UserPublic

class ReadyServices():

    def __init__(self, conn:ConnectionManager):
        self.conn = conn
        pass
    


    async def joinGame(self):
        
        users = [user.model_dump(include={"id", "name"}) for user in self.conn.users]


        for user in self.conn.users:
            if(user.id == self.conn.users[0].id):
                await self.conn.send_command({'action':True,'users':users},user.webSocket)
            else:
                await self.conn.send_command({'action':False,'users':users},user.webSocket)
        
        ...
