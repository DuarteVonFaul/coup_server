from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
from connection.connectionManage import manager
from models.services.readyServices import ReadyServices


app = FastAPI()


@app.websocket("/ws/{client_id}/{username}")
async def websocket_endpoint(websocket:WebSocket, client_id: int, username:str):
    await manager.connect(client_id,username,websocket)
    try:
        while True:
            data = json.loads(await websocket.receive_text())
            print(data)
            if(data['type']=='lobby'):
                await ReadyServices(manager).joinGame()
            elif(data['type']=='ready'):
                await ReadyServices(manager).ready()
            elif(data['type']=='Action'):
                ...
            await manager.broadcast()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast()



@app.websocket("/ws/ready{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    try: 
        
        ...
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast()
