"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import sys
from homework_04 import models, jsonplaceholder_requests as jsr


async def create_tables():
    async with models.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)


async def get_users(userdata, postdata):
    async with models.Session() as session:
        async with session.begin():
            for user in userdata:
                user = models.User(name=user['name'], username=user['username'], email=user['email'])
                session.add(user)
            for post in postdata:
                post = models.Post(user_id=post['userId'], title=post['title'], body=post['body'])
                session.add(post)


async def async_main():
    await create_tables()
    userdata, postdata = await asyncio.gather(jsr.fetch_json(jsr.USERS_DATA_URL), jsr.fetch_json(jsr.POSTS_DATA_URL))
    await get_users(userdata, postdata)


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
