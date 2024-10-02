import asyncio
import logging
import sys
import handlers
from data.config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

dp = Dispatcher()




async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    handlers.setup(dp)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
      asyncio.run(main())
    except KeyboardInterrupt:
       print('Exit')