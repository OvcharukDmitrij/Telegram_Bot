from logger.bot_logger import logging
from main import session, bot
from models import User

# Укажите текст, который бот отправит всем пользователям из БД
text = 'Testing'

try:
    users = session.query(User).all()
    if not users:
        logging.info('В БД отсутствуют пользователи.')
    else:
        for user in users:
            bot.send_message(user.telegram_id, text)
        logging.info('Сообщения отправлены пользователям.')
except Exception as error:
    logging.error(error)
