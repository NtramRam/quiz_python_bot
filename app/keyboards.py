from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
  [InlineKeyboardButton(text="Корзина", callback_data='basket'), 
   InlineKeyboardButton(text="Контакты", callback_data='contacts')]
], resize_keyboard = True, input_field_placeholder='Жмай кнопки, блять!')

setting = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='VK', url='https://vk.com/nitram_ram'), InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/channel/UCE_SuiburtjwAcusRtMqx_w')],
  [InlineKeyboardButton(text='Telegram', url='https://t.me/senot_snitram')]
])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                            request_contact=True)]],
                                                            resize_keyboard=True)

nums = ['1', '2', '3', '4']

async def inline_nums():
  keyboard = InlineKeyboardBuilder()
  for n in nums:
    keyboard.add(InlineKeyboardButton(text=n, url='https://t.me/senot_snitram'))
  return keyboard.adjust(2).as_markup()