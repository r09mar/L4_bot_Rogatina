from aiogram import Bot, Dispatcher, types, Router, filters, F
import asyncio
import token

API_TOKEN = token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
start_router = Router()

@start_router.message(filters.CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я - echo bot. Напиши мне что-нибудь и я повторю")

@start_router.message(F.text)
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())