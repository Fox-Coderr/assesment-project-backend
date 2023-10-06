from pydantic import BaseModel
from datetime import datetime


class RoomCreate(BaseModel):
    name: str


class MessageCreate(BaseModel):
    room_id: int
    nickname: str
    message_text: str
    timestamp: datetime


class Message(BaseModel):
    room_id: int
    nickname: str
    message_text: str
    timestamp: datetime
