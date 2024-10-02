from aiogram import Dispatcher

from handlers import users


def setup(dp: Dispatcher):
    users.setup(dp)