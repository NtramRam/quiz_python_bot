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
   InlineKeyboardButton(text='Тест: "Pass"', callback_data='pass'),], 
  [InlineKeyboardButton(text='В главное меню', callback_data='back_main')]
], resize_keyboard = True, input_field_placeholder='Выбирай тест и погнали!')

naruto_1 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Отсутствует', callback_data=MyCallback(foo='srn', bar = 1).pack())],
  [InlineKeyboardButton(text='Низкая', callback_data=MyCallback(foo='srn', bar = 2).pack())],
  [InlineKeyboardButton(text='В норме', callback_data=MyCallback(foo='srn', bar = 3).pack())],
  [InlineKeyboardButton(text='Высокая', callback_data=MyCallback(foo='srn', bar = 4).pack())],
  [InlineKeyboardButton(text='Я лучше всех', callback_data=MyCallback(foo='srn', bar = 5).pack())]])

naruto_2 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Это я виноват', callback_data=MyCallback(foo='hn', bar = 1).pack())],
  [InlineKeyboardButton(text='Я это заслужил', callback_data=MyCallback(foo='hn', bar = 2).pack())],
  [InlineKeyboardButton(text='Пофиг', callback_data=MyCallback(foo='hn', bar = 3).pack())],
  [InlineKeyboardButton(text='Это его вина', callback_data=MyCallback(foo='hn', bar = 4).pack())],
  [InlineKeyboardButton(text='Месть', callback_data=MyCallback(foo='hn', bar = 5).pack())]])

naruto_3 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Не вижу смысла', callback_data=MyCallback(foo='ln', bar = 1).pack())],
  [InlineKeyboardButton(text='Учусь, потому что надо', callback_data=MyCallback(foo='ln', bar = 2).pack())],
  [InlineKeyboardButton(text='Без особого энтузиазма', callback_data=MyCallback(foo='ln', bar = 3).pack())],
  [InlineKeyboardButton(text='Люблю учиться', callback_data=MyCallback(foo='ln', bar = 4).pack())],
  [InlineKeyboardButton(text='Считаю это очень важным', callback_data=MyCallback(foo='ln', bar = 5).pack())]])

naruto_4 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Защищаю близких', callback_data=MyCallback(foo='dn', bar = 1).pack())],
  [InlineKeyboardButton(text='Хлоднокровие', callback_data=MyCallback(foo='dn', bar = 2).pack())],
  [InlineKeyboardButton(text='Использую тактику', callback_data=MyCallback(foo='dn', bar = 3).pack())],
  [InlineKeyboardButton(text='В бой!', callback_data=MyCallback(foo='dn', bar = 4).pack())],
  [InlineKeyboardButton(text='Ищу слабые места и атакую', callback_data=MyCallback(foo='dn', bar = 5).pack())]])

naruto_5 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Карьера', callback_data=MyCallback(foo='drn', bar = 1).pack())],
  [InlineKeyboardButton(text='Сила', callback_data=MyCallback(foo='drn', bar = 2).pack())],
  [InlineKeyboardButton(text='Семья', callback_data=MyCallback(foo='drn', bar = 3).pack())],
  [InlineKeyboardButton(text='Признание', callback_data=MyCallback(foo='drn', bar = 4).pack())],
  [InlineKeyboardButton(text='Гармония', callback_data=MyCallback(foo='drn', bar = 5).pack())]])

naruto_over = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Вернуться к выбору тестов', callback_data='tests')]])