from aiogram import executor

from handlers.users.sending import news
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    try:
        await db.create_table_companies()
    except Exception as err:
        print(err)

    try:
        await db.create_table_users()
    except Exception as error:
        print(error)

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    dp.loop.create_task(news())
    executor.start_polling(dp, on_startup=on_startup)

