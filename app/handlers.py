from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
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

@router.message(CommandStart())
async def cmd_start(message: Message):
  await rq.set_user(message.from_user)
  await message.answer(f'Узнай кто ты из Наруто!', reply_markup=kb.main)

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

@router.message(Command('give_photo'))
async def give_photo(message: Message):
  await message.answer_photo(photo='AgACAgIAAxkBAAMWZkUAAcrX4630iVFDyO3bb-zLkBs8AAIP3jEbHGwpSqz7po9qHJJzAQADAgADeAADNQQ',
                             caption='Это рисунок лица')

@router.message(F.photo)
async def get_photo(message: Message):
  await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
  await callback.answer('FFFF', show_alert=True)
  await callback.message.edit_text('Привет!', reply_markup=await kb.inline_nums())


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
  await state.set_state(Reg.name)
  await message.answer('Введите Ваше имя')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
  await state.update_data(name=message.text)
  await state.set_state(Reg.number)
  await message.answer('Введите номер телефона', reply_markup=kb.get_number)

@router.message(Reg.number, F.contact)
async def reg_three(message: Message, state: FSMContext):
  await state.update_data(number=message.contact.phone_number)
  data = await state.get_data()
  await message.answer(f'Спасибо, регистрация завершена. \nИмя: {data["name"]}\nНомер: {data["number"]}')
  await state.clear()