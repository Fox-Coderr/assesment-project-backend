from api import rooms, messages, websocket
from api.config import app

app.include_router(rooms.router)
app.include_router(messages.router)
app.mount("/", websocket.app)
