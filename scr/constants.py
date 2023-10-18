from main import session
from models import Message

DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
ALL_NUM_MASSAGE = session.query(Message).count()
COURSE_COMPLETED = "Все сообщения получены!"
WAIT_MONDAY = "Доступ к новым материалам откроется в следующий понедельник."
WELCOME_BACK = '{}, мы рады вновь видеть тебя!'
GREETING = 'Привет, {}! Мы рады тебя приветствовать!!! Нажимай кнопку "далее" и начнешь получать сообщения.'