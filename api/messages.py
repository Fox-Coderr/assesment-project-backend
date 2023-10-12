from fastapi import APIRouter
from database.models import Message
from database.session_manager import create_session
from database import schemas

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{room_id}/", response_model=list[schemas.Message])
def get_messages(room_id):
    session = create_session()
    messages = session.query(Message).filter_by(room_id=room_id).all()
    session.close()
    return messages