from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai

load_dotenv()
API_Token = os.getenv("TELEGRAM_BOT_TOKEN")
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPEN_API_KEY

MODEL_NAME = "gpt-3.5-turbo"

bot = Bot(token=API_Token)
dispatcher = Dispatcher(bot)


class Reference:
    def __init__(self) -> None:
        self.response = ""


reference = Reference()


def clear_past():
    reference.response=""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply(f"Hi!\n I am an echo bot created by Shashank\n How may I assist you today?")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    help_com = """ 
    Hi there, I'm a bot created by Shashank! Use these commands:
    /start - to start the conversation
    /clear - to clear the past convo
    /help - to get help.
    """
    
    await message.reply(help_com)

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler receives messages with `/clear` command
    """
    clear_past()
    
    await message.reply("I've cleared the past conversation and context!")


@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    This handler receives messages with `/clear` command
    """
    print(f">>> User :\n\t{message.text}")

    response = openai.ChatCompletion.create(
        model =MODEL_NAME,
        messages = [
            {"role":"assistant", "content": reference.response},
            {"role":"user", "content": message.text}
        ]
    )

    reference.response = response['choices'][0]['message']['content']
    print(f">>>chatGPT: \n\t{reference.response}")
    
    await bot.send_message(chat_id=message.chat.id, text= reference.response)



if __name__ == "__main__":
    executor.start_polling(dispatcher,skip_updates=True)
