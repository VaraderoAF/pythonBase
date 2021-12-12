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
from homework_04 import models, jsonplaceholder_requests as jsr


async def create_tables():
    async with models.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)


async def get_users(userdata):
    async with models.Session() as session:
        async with session.begin():
            for user in userdata:
                name = user['name']
                username = username['username']
                email = user['email']
                user = models.User(name=name, username=username, email=email)
                session.add(user)


async def get_posts(postdata):
    async with models.Session() as session:
        async with session.begin():
            for post in postdata:
                user_id = post['userId']
                title = post['title']
                body = post['body']
                post = models.Post(title=title, body=body, user_id=user_id)
                session.add(post)


async def async_main():
    await create_tables()
    userdata = await asyncio.gather(jsr.fetch_json(jsr.USERS_DATA_URL))
    postdata = await asyncio.gather(jsr.fetch_json(jsr.POSTS_DATA_URL))
    await get_users(userdata)
    await get_posts(postdata)



def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
