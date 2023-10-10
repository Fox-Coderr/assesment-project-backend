from fastapi import WebSocket, WebSocketDisconnect
from fastapi import FastAPI
from database.models import create_message
import json

app = FastAPI()
connected_clients = {}


@app.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str):
    await websocket.accept()
    if room_name not in connected_clients:
        connected_clients[room_name] = set()
    connected_clients[room_name].add(websocket)
    try:
        while True:
            json_message = await websocket.receive_text()
            message = json.loads(json_message)
            create_message(message)
            for client in connected_clients[room_name]:
                await client.send_text(json_message)
    except WebSocketDisconnect:
        connected_clients[room_name].remove(websocket)
        if not connected_clients[room_name]:
            del connected_clients[room_name]