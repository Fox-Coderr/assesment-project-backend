from fastapi import APIRouter
from database.models import ChatRoom
from database.session_manager import create_session
from database import schemas

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def create_room(room: schemas.RoomCreate):
    session = create_session()
    chat_room = ChatRoom(room_name=room.name)
    session.add(chat_room)
    session.commit()
    session.close()


@router.get("/")
def get_rooms():
    session = create_session()
    chat_rooms = session.query(ChatRoom).all()
    session.close()
    return {'chat_rooms': chat_rooms}

