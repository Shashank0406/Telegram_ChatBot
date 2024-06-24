from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

#init bot

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

 
@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply(f"Hi!\n I am an echo bot powered by AIOGRAM\n Hi ra Aravind lanja munda")

@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply(message.text)





if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)