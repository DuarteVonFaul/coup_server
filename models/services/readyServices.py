from connection.connectionManage import ConnectionManager
from models.schemas.playerSchema   import PlayerScheme

class ReadyServices():

    def __init__(self, conn:ConnectionManager):
        self.conn = conn
        pass
    


    async def joinGame(self):
        
        users = [user.model_dump(include={"id", "name"}) for user in self.conn.users]


        for user in self.conn.users:
            if(user.id == self.conn.users[0].id):
                await self.conn.send_command({'commad':0,'data':users},user.webSocket)
            else:
                await self.conn.send_command({'commad':1,'data':users},user.webSocket)

    async def ready(self):

        self.conn.ready()
        players = []
        for user in self.conn.users:
            players.append(PlayerScheme(id=user.id, name=user.name, coins=user.player.coins, letters=user.player.Letters))

        
        for user in self.conn.users:
            if(user.id == self.conn.users[0].id):
                players_dict = [player.model_dump() for player in players]
                await self.conn.send_command({'commad':2,'data':players_dict},user.webSocket)
            else:
                await self.conn.send_command({'commad':3,'data':players.__dict__},user.webSocket)
        

        

    async def Game(self, action):
        
        users = [user.model_dump(include={"id", "name"}) for user in self.conn.users]


        for user in self.conn.users:
            if(user.id == self.conn.users[0].id):
                await self.conn.send_command({'commad':0,'data':users},user.webSocket)
            else:
                await self.conn.send_command({'commad':1,'data':users},user.webSocket)        
        
        ...
