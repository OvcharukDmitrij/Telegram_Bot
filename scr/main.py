import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from telegram import Bot

from models import Base

engine = create_engine('sqlite:///sqlite.db')
session = Session(engine)
Base.metadata.create_all(engine)

load_dotenv()

secret_token = os.getenv('TOKEN')
owner_id = os.getenv('OWNER_ID')

bot = Bot(token=secret_token)
