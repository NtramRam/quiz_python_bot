from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ContentType, FSInputFile, InputMediaPhoto
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware
import app.database.requests as rq

router = Router()

router.message.outer_middleware(TestMiddleware())


class Reg(StatesGroup):
  name = State()
  number = State()

class Nar(StatesGroup):
  data = State()

class NarTest(StatesGroup):
  user_tg_id = State()
  self_rating = State()
  hurt = State()
  learning = State()
  danger = State()
  dream = State()

# ONLY FOR TEST
@router.message(Command('test'))
async def cmd_test(message: Message):
    await message.answer(f'Нет тестового задания')


# MAIN PART OF THE TEST
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
  await rq.set_user(message.from_user)
  await state.set_state(NarTest.user_tg_id)
  await state.update_data(user_tg_id = message.from_user.id)
  await message.answer_photo(photo='https://docs.google.com/uc?id=1nstYTnhATbX197iw5U2xwNBWntnTJoj2', caption=f'Добро пожаловать в UltraTestBot!', reply_markup=kb.main)
  print(f'зарегестрирован новый пользователь {message.from_user.username}')

# test functions
@router.callback_query(F.data == 'tests')
async def n_stars(callback: CallbackQuery):
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1ogMxiyg6UgBZzhQMyra_AfO8tb7Ymtiu'))
  await callback.message.edit_caption(caption=f'Выбирай тест и погнали!', reply_markup=kb.tests)

@router.callback_query(F.data == 'test_naruto') 
async def n_1(callback: CallbackQuery, state: FSMContext):
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH'))
  await callback.message.edit_caption(caption=f'Твоя самооценка?', reply_markup=kb.naruto_1)

@router.callback_query(kb.MyCallback.filter(F.foo == 'srn'))  
async def n_2(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarTest.self_rating)
  await state.update_data(self_rating = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Отношение к обиде?', reply_markup=kb.naruto_2)

@router.callback_query(kb.MyCallback.filter(F.foo == 'hn'))
async def n_3(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarTest.hurt)
  await state.update_data(hurt = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Отношение к учёбе?', reply_markup=kb.naruto_3)


@router.callback_query(kb.MyCallback.filter(F.foo == 'ln'))
async def n_4(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarTest.learning)
  await state.update_data(learning = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Как поступишь в опасной ситуации?', reply_markup=kb.naruto_4)

@router.callback_query(kb.MyCallback.filter(F.foo == 'dn'))
async def n_5(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarTest.danger)
  await state.update_data(danger = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'С чем связанна главная мечта?', reply_markup=kb.naruto_5)

@router.callback_query(kb.MyCallback.filter(F.foo == 'drn'))
async def n_over(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarTest.dream)
  await state.update_data(dream = callback.data[-1])
  n_data = await state.get_data()
  await rq.set_n_data(n_data)
  await state.clear()
  await callback.answer()
  await callback.message.edit_reply_markup(f'Поздравляю, ты *имя_персонажа*\n*описание_характера*\n*уникальный_токен*')
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Поздравляю, ты *имя_персонажа*\n*описание_характера*\n*уникальный_токен*') #UPL markup


# OTHER FUNCS
@router.message(Command('naruto'))
async def add_naruto(message: Message, state: FSMContext):
  await state.set_state(Nar.data)
  await message.answer(f'Введи данные в формате:\nимя интелект сила ловкость энергия')

@router.message(Nar.data)
async def over_naruto(message: Message, state: FSMContext):
  await rq.ch_naruto(message.text)
  await message.answer(f'Все готово, проверяй базу данных\n{message.text.split(' ')}')
  await state.clear()

@router.message(Command('info'))
async def get_info(message: Message):
  info = str(message.from_user).split(' ')
  upinfo = ''
  for i in info:
    upinfo += f'{i}\n'
  await message.answer(f'{upinfo}')

@router.message(Command('help'))
async def get_help(message: Message):
  await message.answer(f'/start - запустит бота\n/give_photo - отправит фото лица\nКак дела? - ответит Хорошо, а твои?')

@router.message(F.text == 'Наруто 15 30 30 48')
async def how_are_you(message: Message):
  info = message.text.split(' ')
  await message.answer(f'Вот твоя строка:\n{info}')