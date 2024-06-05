from sqlalchemy import BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, relationship, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username = mapped_column(String)
    first_name = mapped_column(String)

class Character(Base):
    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    self_rating: Mapped[int] = mapped_column(Integer)
    hurt: Mapped[int] = mapped_column(Integer)
    learning: Mapped[int] = mapped_column(Integer)
    danger: Mapped[int] = mapped_column(Integer)
    dream: Mapped[int] = mapped_column(Integer)

class UserCharacter(Base): 
    __tablename__ = 'user_characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id = mapped_column(BigInteger)
    self_rating: Mapped[str] = mapped_column(String)
    hurt: Mapped[str] = mapped_column(String)
    learning: Mapped[str] = mapped_column(String)
    danger: Mapped[str] = mapped_column(String)
    dream: Mapped[str] = mapped_column(String)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)