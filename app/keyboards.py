from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Психологические тесты', callback_data='tests')],
  [InlineKeyboardButton(text='"Pass"', callback_data='pass'), 
   InlineKeyboardButton(text='"Pass"', callback_data='pass')]
], resize_keyboard = True)

tests = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Тест: "Кто ты из Наруто?"', callback_data='test_naruto')],
  [InlineKeyboardButton(text='Тест: "Pass"', callback_data='pass'), 
   InlineKeyboardButton(text='Тест: "Pass"', callback_data='pass')]
], resize_keyboard = True, input_field_placeholder='Выбирай тест и погнали!')

naruto_1 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='s_r 1', callback_data=MyCallback(foo='srn', bar = 1).pack())],
  [InlineKeyboardButton(text='s_r 2', callback_data=MyCallback(foo='srn', bar = 2).pack())],
  [InlineKeyboardButton(text='s_r 3', callback_data=MyCallback(foo='srn', bar = 3).pack())],
  [InlineKeyboardButton(text='s_r 4', callback_data=MyCallback(foo='srn', bar = 4).pack())],
  [InlineKeyboardButton(text='s_r 5', callback_data=MyCallback(foo='srn', bar = 5).pack())]])

naruto_2 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='h 1', callback_data=MyCallback(foo='hn', bar = 1).pack())],
  [InlineKeyboardButton(text='h 2', callback_data=MyCallback(foo='hn', bar = 2).pack())],
  [InlineKeyboardButton(text='h 3', callback_data=MyCallback(foo='hn', bar = 3).pack())],
  [InlineKeyboardButton(text='h 4', callback_data=MyCallback(foo='hn', bar = 4).pack())],
  [InlineKeyboardButton(text='h 5', callback_data=MyCallback(foo='hn', bar = 5).pack())]])

naruto_3 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='l 1', callback_data=MyCallback(foo='ln', bar = 1).pack())],
  [InlineKeyboardButton(text='l 2', callback_data=MyCallback(foo='ln', bar = 2).pack())],
  [InlineKeyboardButton(text='l 3', callback_data=MyCallback(foo='ln', bar = 3).pack())],
  [InlineKeyboardButton(text='l 4', callback_data=MyCallback(foo='ln', bar = 4).pack())],
  [InlineKeyboardButton(text='l 5', callback_data=MyCallback(foo='ln', bar = 5).pack())]])

naruto_4 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='d 1', callback_data=MyCallback(foo='dn', bar = 1).pack())],
  [InlineKeyboardButton(text='d 2', callback_data=MyCallback(foo='dn', bar = 2).pack())],
  [InlineKeyboardButton(text='d 3', callback_data=MyCallback(foo='dn', bar = 3).pack())],
  [InlineKeyboardButton(text='d 4', callback_data=MyCallback(foo='dn', bar = 4).pack())],
  [InlineKeyboardButton(text='d 5', callback_data=MyCallback(foo='dn', bar = 5).pack())]])

naruto_5 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='dr 1', callback_data=MyCallback(foo='drn', bar = 1).pack())],
  [InlineKeyboardButton(text='dr 2', callback_data=MyCallback(foo='drn', bar = 2).pack())],
  [InlineKeyboardButton(text='dr 3', callback_data=MyCallback(foo='drn', bar = 3).pack())],
  [InlineKeyboardButton(text='dr 4', callback_data=MyCallback(foo='drn', bar = 4).pack())],
  [InlineKeyboardButton(text='dr 5', callback_data=MyCallback(foo='drn', bar = 5).pack())]])