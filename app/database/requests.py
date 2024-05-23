from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import  select, update, delete

async def set_user(user_info):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == user_info.id))

    if not user:
        session.add(User(tg_id = user_info.id, username = user_info.username, first_name = user_info.first_name))
        await session.commit()