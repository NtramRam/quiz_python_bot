from app.database.models import async_session
from app.database.models import User, UserCharacter
from sqlalchemy import  select, update, delete

async def set_user(user_info):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == user_info.id))

    if not user:
        session.add(User(tg_id = user_info.id, username = user_info.username, first_name = user_info.first_name))
        await session.commit()

async def set_n_data(n_data):
    async with async_session() as session:
        session.add(UserCharacter(user_tg_id = n_data['user_tg_id'], self_rating = n_data['self_rating'], 
                      hurt = n_data['hurt'], learning = n_data['learning'], danger = n_data['danger'], dream = n_data['dream']))
        await session.commit()

