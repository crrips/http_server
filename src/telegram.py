from aiogram import Bot, Dispatcher
from config.config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def send_notification_to_telegram(message, identifier):
    print(f"Notification sent for identifier {identifier}")
    await bot.send_message(ADMIN_ID, message)
