from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.subs import subscribe_callback, unsubscribe_callback


async def create_button_subscribe(message: types.Message):
    subscribe_button = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text="Подписка на новости",
                                                        callback_data=subscribe_callback.new(yes="yes",
                                                                                             comp=f"{message.text}")
                                                    )
                                                ]
                                            ])
    return subscribe_button


async def create_button_unsubscribe(company: str):
    company = company.upper()
    unsubscribe_button = InlineKeyboardMarkup(row_width=1,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(
                                                          text=f"Отписаться от новостей по {company}",
                                                          callback_data=unsubscribe_callback.new(no="no", comp=company)
                                                      )
                                                  ]
                                              ])
    return unsubscribe_button
