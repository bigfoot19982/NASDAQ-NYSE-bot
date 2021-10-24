from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.subs import affirm_callback, unsubs_callback


async def create_but(message: types.Message):
    news_on_the_stock = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text="Подписка на новости",
                                                         callback_data=affirm_callback.new(yes="yes",
                                                                                           comp=f"{message.text}")
                                                     )
                                                 ]
                                             ])
    return news_on_the_stock

async def create_but2(company: str):
    company = company.upper()
    unsubs = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text=f"Отписаться от новостей по {company}",
                                              callback_data=unsubs_callback.new(no="no", comp=company)
                                          )
                                      ]
                                  ])
    return unsubs