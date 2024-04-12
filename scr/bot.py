from telegram import ReplyKeyboardMarkup
from telegram.constants import PARSEMODE_HTML
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

from constants import (ALL_NUM_MASSAGE, COURSE_COMPLETED,
                       WELCOME_BACK, GREETING)
from logger.bot_logger import logging
from main import session, secret_token, bot, owner_id
from models import User
from views import get_message


def wake_up(update, context):
    """Обработчик для команды '/start'."""
    try:
        chat = update.effective_chat
        name = update.message.chat.first_name
        button = ReplyKeyboardMarkup([['далее']], resize_keyboard=True)
        text = f'{name}! ' + COURSE_COMPLETED
        user = session.query(User).filter_by(
            telegram_id=update.message.chat.id
        ).first()
        if user and user.current_message <= ALL_NUM_MASSAGE:
            text = WELCOME_BACK.format(name)
        if not user:
            user = User(
                telegram_id=update.message.chat.id,
                username=update.message.chat.username,
                name=update.message.chat.first_name,
                surname=update.message.chat.last_name
            )
            session.add(user)
            session.commit()
            text = GREETING.format(name)

        context.bot.send_message(
            chat_id=chat.id,
            text=text,
            reply_markup=button
        )
        logging.info(f'Пользователю {chat.id} отправлено сообщение "{text}"')
    except Exception as error:
        logging.error(error)


def messages(update, context):
    """Обработчик для кнопки 'далее'."""
    try:
        chat = update.effective_chat
        button = ReplyKeyboardMarkup([['далее']], resize_keyboard=True)
        message = get_message(update.message.chat.id)

        context.bot.send_message(
            chat_id=chat.id,
            text=message,
            parse_mode=PARSEMODE_HTML,
            reply_markup=button
        )
        logging.info(f'Пользователю {chat.id} отправлено сообщение {message}')
    except Exception as error:
        logging.error(error)


def restart(update, context):
    """Функция позволяет пользователю получить все сообщения сначала."""
    user = session.query(User).filter_by(
        telegram_id=update.message.chat.id
    ).first()
    user.current_message = 1
    session.add(user)
    session.commit()


def main():
    logging.info('Бот запущен.')
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('restart', restart))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, messages))

    updater.start_polling()
    updater.idle()
    bot.send_message(owner_id, 'Бот остановлен.')
    logging.info('Бот остановлен.')


if __name__ == '__main__':
    main()
