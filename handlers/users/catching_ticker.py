from aiogram import types

from keyboards.inline.news import create_but, create_but2
from keyboards.inline.subs import affirm_callback, unsubs_callback
from loader import dp, db
from utils.parsing.receiving_tickers import func


@dp.message_handler()
async def get_ticker(message: types.Message):
    data = await func(message.text)
    if (len(data) == 5):
        await dp.bot.send_photo(message.from_user.id, photo=data[3], caption=
        f"{data[2]}\n"
        f"\n"
        f"{data[-1]}\n"
        f"\n"
        f"Цена акции {data[0]}$.\n"
        f"Капитализация {data[1][0]}$.\n"
        f"Общая выручка {data[1][1]}$\n"
        f"Чистый доход {data[1][2]}$\n"
        f"P/E равен {data[1][3]} (в норме он меньше 15)\n"
        f"Дивиденды составляют {data[1][4]}\n"
        f"Потенциал роста до {data[1][5]}.\n", reply_markup=await create_but(message))
    else:
        await dp.bot.send_message(message.from_user.id, f"{data[2]}\n"
                                                        f"\n"
                                                        f"{data[-1]}\n"
                                                        f"\n"
                                                        f"Цена акции {data[0]}$.\n"
                                                        f"Капитализация {data[1][0]}$.\n"
                                                        f"Общая выручка {data[1][1]}$\n"
                                                        f"Чистый доход {data[1][2]}$\n"
                                                        f"P/E равен {data[1][3]} (в норме он меньше 15)\n"
                                                        f"Дивиденды составляют {data[1][4]}\n"
                                                        f"Потенциал роста до {data[1][5]}.\n",
                                  reply_markup=await create_but(message))


@dp.callback_query_handler(affirm_callback.filter(yes="yes"))
async def affirmation(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    company = (callback_data.get("comp")).upper()
    await db.add_company(company)
    user_name = call.from_user.first_name
    b = await db.add_user(call.from_user.id, company, user_name, call)
    if b != False:
        await call.message.answer(f"Вы подписались на новости про {company}!\n"
                                  f"Чтобы отписаться, нажмите соответствующую кнопку",
                                  reply_markup=await create_but2(company))


@dp.callback_query_handler(unsubs_callback.filter(no="no"))
async def unsubscription(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    company = callback_data.get("comp")
    await db.unsubscribe(call.from_user.id, company)
    await call.message.answer(text=f"Вы отказались от подписки на {company}!")
