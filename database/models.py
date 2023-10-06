from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database.session_manager import create_session
from database.config import engine


Base = declarative_base()


def create_message(message):
    session = create_session()
    new_message = Message(
        room_id=int(message['room']),
        nickname=message['nickname'],
        message_text=message['message_text'],
        timestamp=message['timestamp']
    )
    session.add(new_message)
    session.commit()
    session.close()


class ChatRoom(Base):
    __tablename__ = 'chat_rooms'

    id = Column(Integer, primary_key=True)
    room_name = Column(String(255), unique=True, nullable=False)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('chat_rooms.id'), nullable=False)
    nickname = Column(Text,nullable=False)
    message_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    chat_room = relationship('ChatRoom')


#should be removed?
Base.metadata.create_all(engine)
