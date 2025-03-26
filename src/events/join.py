from highrise.models import User
from config.config import loggers


async def on_join(bot, user: User) -> None:
    if loggers.joins:
        print(f"User joined: {user.username}:{user.id}")
    await bot.highrise.chat(f"{user.username} Присоеденился к нам!")
