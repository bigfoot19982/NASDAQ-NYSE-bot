from aiogram import types

from handlers.users.supplementary.get_company_data_text import form_text
from keyboards.inline.news import create_button_subscribe, create_button_unsubscribe
from keyboards.inline.subs import subscribe_callback, unsubscribe_callback
from loader import dp, db
from utils.parsing.get_primary_data_on_a_stock import getting_info_on_the_ticker


# try sending the stock info with pic, then, if failed (sometimes there is no
# picture on the site we parse data from), retry with no picture
async def answer_to_ticker(data: list, message: types.Message):
    try:
        await dp.bot.send_photo(message.from_user.id, photo=data[4], caption=await form_text(data),
                                reply_markup=await create_button_subscribe(message))
    except:
        await dp.bot.send_message(message.from_user.id, text=await form_text(data),
                                  reply_markup=await create_button_subscribe(message))


# we receive a ticker of a company, collecting all the data on the stock and launch answer func
@dp.message_handler()
async def get_ticker(message: types.Message):
    data = await getting_info_on_the_ticker(message.text)
    await answer_to_ticker(data, message)


# if users pressed subscription button we add him to the DB and inform him about the subscription
# we also give him an opportunity to unsubscribe
@dp.callback_query_handler(subscribe_callback.filter(yes="yes"))
async def subscription(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    company = (callback_data.get("comp")).upper()
    await db.add_company(company)
    user_name = call.from_user.first_name
    b = await db.add_user(call.from_user.id, company, user_name, call)
    if b != False:
        await call.message.answer(f"Вы подписались на новости про {company}!\n"
                                  f"Чтобы отписаться, нажмите соответствующую кнопку",
                                  reply_markup=await create_button_unsubscribe(company))

# on pressing unsubscribe button we delete user from the DB
@dp.callback_query_handler(unsubscribe_callback.filter(no="no"))
async def unsubscription(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    company = callback_data.get("comp")
    await db.unsubscribe(call.from_user.id, company)
    await call.message.answer(text=f"Вы отказались от подписки на {company}!")
