from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from connection.connectionManage import manager


app = FastAPI()


@app.websocket("/ws/{client_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, username:str):
    await manager.connect(client_id,username,websocket)
    try: 
        if(manager.users[0].id == client_id):
            await manager.send_personal_message("Player Ready",websocket=websocket)
        data = await websocket.receive_text()
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
