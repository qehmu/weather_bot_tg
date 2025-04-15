import asyncio
import logging
import requests
from aiogram import (Bot, Dispatcher)
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

TOKEN = '6430541813:AAFOBJW62aO6DW29SguGyCbscy0fZYZIMfg'
API = '3d9de74844d28377e81415151cbe6a66'
dp = Dispatcher(storage=MemoryStorage())


def isCityExists(city):
    weather_info = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric').json()
    code_https = weather_info['cod']
    return True if code_https == 200 else False


# функция проверяет, существует ли город, возвращает булевое значение
def get_weather(city):
    weather_info = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric').json()
    feels_like = weather_info['main']['feels_like']
    main_temperature = weather_info['main']['temp']
    wind_speed = weather_info['wind']['speed']
    wind_deg = weather_info['wind']['deg']
    wind_gust = weather_info['wind']['gust']
    name = weather_info['name']
    code_of_https = weather_info['cod']
    return main_temperature, feels_like, wind_gust, wind_deg, wind_speed, name, code_of_https


# функция, запрашивающая данные о погоде, указанном юзером
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Напиши название города, и я предоставлю данные о погоде там. В некоторых случаях, надо уточнять, где находится город")


@dp.message()
async def check_city(message: Message):
    user_city = message.text
    try:
        if isCityExists(user_city):
            weather_data = get_weather(user_city)
            await message.answer(
                f"Данные по погоде в {user_city}:\nТемпература: {weather_data[1]}°C\nОщущается как: {weather_data[0]}°C\nСкорость ветра; порывами до: {weather_data[2]}; {weather_data[4]} м/с\nКод_https: {weather_data[6]}")
        else:
            await message.answer("Увы, мне не удалось найти то, что вы хотели. Попробуйте уточнить название.")
    except False:
        return False


# except позволяет обходить ошибки, что обеспечивает стабильную работу бота
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(main())
