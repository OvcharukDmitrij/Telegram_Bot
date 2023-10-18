from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from logger.bot_logger import logging
from constants import (DATE_FORMAT, ALL_NUM_MASSAGE,
                       COURSE_COMPLETED, WAIT_MONDAY)
from main import session
from models import User, Message


def render_message(text=None, message=None):
    try:
        fileloader = FileSystemLoader('templates')
        env = Environment(loader=fileloader)
        tm = env.get_template('message.html')
        msg = tm.render(text=text, message=message)
        return msg
    except Exception as error:
        logging.error(error)


def get_message(user_id):
    try:
        user = session.query(User).filter_by(telegram_id=user_id).first()
        num_current_message_for_user = user.current_message
        if num_current_message_for_user > ALL_NUM_MASSAGE:
            return render_message(text=COURSE_COMPLETED)
        message = session.query(Message).filter_by(
            id=num_current_message_for_user
        ).first()
        if datetime.now() < datetime.strptime(
                message.opening_date, DATE_FORMAT
        ):
            return render_message(text=WAIT_MONDAY)
        user.current_message += 1
        session.commit()
        return render_message(message=message)
    except Exception as error:
        logging.error(error)
