from app.database.models import async_session
from app.database.models import User, UserCharacter, Character
from sqlalchemy import  select, update, delete

from random import choice

from secrets import token_hex

from datetime import date, timedelta

#MAIN RQ FUNCTIONS

async def set_user(user_info):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == user_info.id))
    if not user:
        session.add(User(tg_id = user_info.id, username = user_info.username, first_name = user_info.first_name))
        session.add(UserCharacter(tg_id = user_info.id, self_rating = 0, hurt = 0, learning = 0, danger = 0, dream = 0, token_nt = 0, lt_day = 0))
        await session.commit()
        print(f'Зарегестрирован новый пользователь {user_info.username}')

async def time_limit(n_data):
    async with async_session() as session:
        user = await session.scalar(select(UserCharacter).where(UserCharacter.tg_id == n_data))
        lt_day = int(user.lt_day)
        today = int((date.today() - date(2024,1,1)).days)
        return today - lt_day

async def set_n_data(n_data):
    async with async_session() as session:
        user_character = await session.scalar(select(UserCharacter).where(UserCharacter.tg_id == n_data['user_tg_id']))
        user_character.self_rating = n_data['self_rating']
        user_character.hurt = n_data['hurt']
        user_character.learning = n_data['learning']
        user_character.danger = n_data['danger']
        user_character.dream = n_data['dream'] 
        user_character.lt_day = n_data['lt_day']     
        await session.commit()
    
async def character_comparison(user_id):
    async with async_session() as session:
        user_data = await session.scalar(select(UserCharacter).where(UserCharacter.tg_id == user_id))
        user_number = user_data.self_rating + user_data.hurt + user_data.learning + user_data.danger + user_data.dream
        list_char = []
        list_num_char = []
        list_num = []
        list_char_over = []
        for i in range(1,6):
            characters_data = await session.scalar(select(Character).where(Character.id == i))
            list_char.append(characters_data.name)
            list_num_char.append(characters_data.self_rating + characters_data.hurt + characters_data.learning + characters_data.danger + characters_data.dream)
        for n in range(5):
            count = 0
            for i in range(5):
                for _ in range(5):
                    if list_num_char[n][i] == user_number[i]:
                        count += 1
                    break
            list_num.append(count)
        max_num = max(list_num)
        for i in range(5):
            if list_num[i] == max_num:
                list_char_over.append(list_char[i])
        return choice(list_char_over)
    
async def character_url_pic(name):
    async with async_session() as session:
        character = await session.scalar(select(Character).where(Character.name == name))
        url_pic = character.url_pic
        return url_pic

async def r_token(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(UserCharacter).where(UserCharacter.tg_id == tg_id))
        character = await session.scalar(select(Character).where(Character.name == name))
        if character.token_switch == 1:
            token = token_hex(7)
            user.token_nt = token
            await session.commit()
            return f'Отличный результат!\n{name} персонаж этой недели!\nТвой токен: {token}\nПокажи токен и получи сюрприз от нас в Ультрамене!'
        else:
            lose_m = 'Отличный результат! Ждем тебя на экзамене чуунина в Ультрамене!'
            return lose_m

#TEST RQ FUNCTIONS
#ONLY FOR DEVELOPER MODE

async def add_character(name, numbs, url_pic): 
    async with async_session() as session:
        character = Character(name = name, self_rating = numbs[0], hurt = numbs[1], learning = numbs[2], danger = numbs[3], dream = numbs[4], url_pic = url_pic, token_switch = 0)
        session.add(character)
        await session.commit()

async def switch_token_character(name):
    async with async_session() as session:
        for i in range(1,6):
            character = await session.scalar(select(Character).where(Character.id == i))
            character.token_switch = 0
        character = await session.scalar(select(Character).where(Character.name == name))
        character.token_switch = 1
        await session.commit()