from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from connection.connectionManage import manager


app = FastAPI()


@app.get("/")
async def get():
    with open("home.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(html_content)



@app.websocket("/ws/{client_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, username:str):
    await manager.connect(client_id,username,websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You {username}: {data}", websocket)
            await manager.broadcast()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast()
