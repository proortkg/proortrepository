import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import start

BOT_TOKEN = "7507650643:AAFY1qKiEPa8JyaKGfrU634L-01QohQfqWU"

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())