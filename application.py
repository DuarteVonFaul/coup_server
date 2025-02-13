from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from connection.connectionManage import manager
from models.services.readyServices import ReadyServices


app = FastAPI()


@app.websocket("/ws/{client_id}/{username}")
async def websocket_endpoint(websocket:WebSocket, client_id: int, username:str):
    await manager.connect(client_id,username,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            if(data=='lobby'):
                await ReadyServices(manager).joinGame()
            elif(data=='ready'):
                await ReadyServices(manager).ready()
            await manager.send_personal_message("Olá {username}",websocket)
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
