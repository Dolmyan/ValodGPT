from aiogram import Bot, Dispatcher
import asyncio
from app.handlers import router

async def main():
    bot= Bot(token='7094241954:AAEazOMKzQw1GhY_I6D0JsW9nbmpt_URjz0')
    dp= Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")