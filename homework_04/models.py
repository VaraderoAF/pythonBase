"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:260295a@localhost/postgres"


engine = create_async_engine(
    PG_CONN_URI,
    echo=False,
)


Base = declarative_base(bind=engine)


Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name={self.name!r}, username={self.username}, email={self.email})'

    def __repr__(self):
        return str(self)

    posts = relationship("Post", back_populates="users")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(256), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    users = relationship("User", back_populates="posts")

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title!r}, body={self.body!r})'

    def __repr__(self):
        return str(self)