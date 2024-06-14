from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ContentType, FSInputFile, InputMediaPhoto
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

from datetime import date
# from app.middlewares import TestMiddleware


router = Router()

#router.message.outer_middleware(TestMiddleware())

class NarQuiz(StatesGroup): # state of "Кто ты из Наруто?" quiz
  user_tg_id = State()
  self_rating = State()
  hurt = State()
  learning = State()
  danger = State()
  dream = State()
  lt_day = State()




# MAIN PART OF THE TEST
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
  await rq.set_user(message.from_user) #sending user information
  await message.answer_photo(photo='https://docs.google.com/uc?id=1nstYTnhATbX197iw5U2xwNBWntnTJoj2', caption=f'Добро пожаловать в UltraTestBot!', reply_markup=kb.main)

# quiz functions
@router.callback_query(F.data == 'back_main')
async def back_main(callback: CallbackQuery):
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1nstYTnhATbX197iw5U2xwNBWntnTJoj2'))
  await callback.message.edit_caption(caption=f'Добро пожаловать в UltraTestBot!', reply_markup=kb.main)
  
@router.callback_query(F.data == 'tests')
async def n_stars(callback: CallbackQuery, state: FSMContext):
  await callback.answer()
  await state.set_state(NarQuiz.user_tg_id) 
  await state.update_data(user_tg_id = callback.from_user.id)
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1ogMxiyg6UgBZzhQMyra_AfO8tb7Ymtiu'))
  await callback.message.edit_caption(caption=f'Выбирай тест и погнали!', reply_markup=kb.tests)

@router.callback_query(F.data == 'test_naruto') 
async def n_1(callback: CallbackQuery, state: FSMContext):
  await callback.answer()
  user = await state.get_data()
  limit_over = await rq.time_limit(callback.from_user.id)
  if limit_over >= 7:
    await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH'))
    await callback.message.edit_caption(caption=f'Твоя самооценка?', reply_markup=kb.naruto_1)
  else:
    await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH'))
    await callback.message.edit_caption(caption=f'Пока ты не можешь пройти тест.\nКоличество дней с последнего теста: {limit_over}', reply_markup=kb.naruto_over)

@router.callback_query(kb.MyCallback.filter(F.foo == 'srn'))  
async def n_2(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarQuiz.self_rating)
  await state.update_data(self_rating = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Отношение к обиде?', reply_markup=kb.naruto_2)

@router.callback_query(kb.MyCallback.filter(F.foo == 'hn'))
async def n_3(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarQuiz.hurt)
  await state.update_data(hurt = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Как относишься к учебе?', reply_markup=kb.naruto_3)

@router.callback_query(kb.MyCallback.filter(F.foo == 'ln'))
async def n_4(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarQuiz.learning)
  await state.update_data(learning = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'Как поступишь в опасной ситуации?', reply_markup=kb.naruto_4)

@router.callback_query(kb.MyCallback.filter(F.foo == 'dn'))
async def n_5(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarQuiz.danger)
  await state.update_data(danger = callback.data[-1])
  await callback.answer()
  await callback.message.edit_media(media=InputMediaPhoto(media='https://docs.google.com/uc?id=1faKN6LZq2IMGZwE3nyW4VyYWlD5OTDpH')) #UPD photo
  await callback.message.edit_caption(caption=f'С чем связанна главная мечта?', reply_markup=kb.naruto_5)

@router.callback_query(kb.MyCallback.filter(F.foo == 'drn'))
async def n_over(callback: CallbackQuery, state: FSMContext):
  await state.set_state(NarQuiz.dream)
  await state.update_data(dream = callback.data[-1])
  await state.set_state(NarQuiz.lt_day)
  await state.update_data(lt_day = (date.today() - date(2024,1,1)).days)
  n_data = await state.get_data()
  await rq.set_n_data(n_data)
  await state.clear()
  await callback.answer()
  user_character = await rq.character_comparison(n_data['user_tg_id'])
  user_character_url_pic = await rq.character_url_pic(user_character)
  user_character_token = await rq.r_token(n_data['user_tg_id'], user_character)
  await callback.message.edit_media(media=InputMediaPhoto(media=user_character_url_pic))
  await callback.message.edit_caption(caption=f'Поздравляю, ты {user_character}!\n\n{user_character_token}', reply_markup=kb.naruto_over) #UPL markup 'BACK MENU'


#ONLY FOR DEVELOPER MODE
@router.message(Command('help'))
async def get_help(message: Message):
  await message.answer('1. /add_ch - добавит пять тестовых персонажей, если базу данных только что создали.\n'
                       '2. /fast_quiz - заполнит данные пользователя единицами (11111)\n'
                       '3. /test - определит персонажа без неоходимости проходить полный квиз (если данные уже заполнены через "fast_quiz" или вручную).\n'
                       '4. /switch Имя - изменить персонажа за которого дается уникальный токен. Пример: [/switch Хината]'
                        )

@router.message(Command('add_ch')) #add limit
async def cmd_add_ch(message: Message):
  gd_url = 'https://docs.google.com/uc?id='
  await rq.add_character('Наруто', '44144', gd_url + '1_Louz1lBPEFiFwvYusapxjlGflf5Iiwm')
  await rq.add_character('Саске', '55422', gd_url + '1hFoOFEKds8zrZNV0NfsLJlqwz7kmirYA')
  await rq.add_character('Какаси', '32555', gd_url + '1Vj90wx_at_N8oNoSO9emnn9ReVBpZOt1')
  await rq.add_character('Хината', '11213', gd_url + '1qnjkE59J7HiDTJgxX0kEO_SQJPORNx_p')
  await rq.add_character('Шикамару', '23331', gd_url + '1O6kzWCM6cEtiv191BsIc07jj0ueXbWwp')
  await message.answer('Добавлено пять персонажей:\n1. Наруто\n2. Саске\n3. Какаси\n4. Хината\n5. Шикамару\n\nМожешь проверять базу данных')

@router.message(Command('fast_quiz'))
async def cmd_fast_quiz(message: Message, state: FSMContext):
    await state.set_state(NarQuiz.user_tg_id) 
    await state.update_data(user_tg_id = message.from_user.id)
    await state.set_state(NarQuiz.self_rating) 
    await state.update_data(self_rating = 1)
    await state.set_state(NarQuiz.hurt) 
    await state.update_data(hurt = 1)
    await state.set_state(NarQuiz.learning) 
    await state.update_data(learning = 1)
    await state.set_state(NarQuiz.danger) 
    await state.update_data(danger = 1)
    await state.set_state(NarQuiz.dream) 
    await state.update_data(dream = 1)
    await state.set_state(NarQuiz.lt_day) 
    await state.update_data(lt_day = (date.today() - date(2024,1,1)).days)
    information = await state.get_data()
    await rq.set_n_data(information)
    await message.answer(f'Данные обновлены успешно!')
    await state.clear()

@router.message(Command('test'))
async def cmd_test(message: Message):
  try:
    user_character = await rq.character_comparison(message.from_user.id)
    user_character_url_pic = await rq.character_url_pic(user_character)
    user_character_token = await rq.r_token(message.from_user.id, user_character)
    await message.answer_photo(photo=user_character_url_pic, caption=f'Твой персонаж это - {user_character}\n{user_character_token}')
  except:
    await message.answer(f'Данные не заполнены!\nИспользуй команду /start или /fast_quiz')

@router.message(Command('switch'))
async def cmd_switch(message: Message):
  try:
    await rq.switch_token_character(message.text.split(' ')[1])
    await message.answer(f'Персонажем этой недели выбран - {message.text.split(' ')[1]}')
  except:
    await message.answer(f'Неправильно введена команду!\nПример: [/switch Хината]')
