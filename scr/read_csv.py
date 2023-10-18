from csv import DictReader

from logger.bot_logger import logging
from main import session
from models import Message

try:
    session.query(Message).delete()
    with open('data/Data.csv', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            message = Message(
                id=row['id'],
                title=row['title'],
                opening_date=row['opening_date'],
                text=row['text'],
                link=row['link'],
                link_name=row['link_name']
            )
            session.add(message)
        session.commit()
    logging.info('БД обновлена.')
except Exception as error:
    logging.error(error)
