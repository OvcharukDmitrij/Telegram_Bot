from datetime import datetime

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """Модель для пользователей из Telegram."""

    __tablename__ = 'users'
    telegram_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    name = Column(String(100))
    surname = Column(String(100))
    date_create = Column(Text, default=datetime.now)
    current_message = Column(Integer, default=1)

    def __str__(self):
        return self.username


class Message(Base):
    """Модель для сообщений."""

    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=True)
    opening_date = Column(Text)
    text = Column(Text, unique=True)
    link = Column(Text, nullable=True)
    link_name = Column(Text, nullable=True)

    def __str__(self):
        return self.text
