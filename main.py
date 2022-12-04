import asyncio
from aiogram import Bot, Dispatcher, types
from io import BytesIO
from os import environ
from httpx import AsyncClient

async def start_handler(event: types.Message):
    await event.answer(
        'hi!',parse_mode=types.ParseMode.HTML
    )

async def cat_handler(event: types.Message):
    async with AsyncClient(trust_env=True) as session:
        result = await session.get(environ['IMAGES_URL'])
        jsoned = result.json()
        picture = await session.get(jsoned[0]['url'])
        buffer = BytesIO()
        buffer.write(picture.content)
        buffer.seek(0)
        await event.answer_photo(buffer,parse_mode=types.ParseMode.HTML)

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