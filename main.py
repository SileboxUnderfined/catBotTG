import asyncio
from aiogram import Bot, Dispatcher, types
from io import BytesIO
from os import environ

async def start_handler(event: types.Message):
    await event.answer(
        'hi!',parse_mode=types.ParseMode.HTML
    )

async def cat_handler(event: types.Message):
    pass

async def main():
    bot = Bot(token=environ['BOT_TOKEN'])
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={'start'})
        disp.register_message_handler(cat_handler, commands={'get_cat'})
        await disp.start_polling()
    finally:
        await bot.close()

if __name__ in "__main__":
    asyncio.run(main())