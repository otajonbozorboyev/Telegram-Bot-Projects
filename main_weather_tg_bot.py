import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Assalomu alaykum! Shaharni kiriting va ob-havoni bilib oling!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Havo ochiq \U00002600",
        "Clouds": "Bulutli \U00002601",
        "Rain" : "Yomg'ir \U00002614",
        "Drizzle" : "Yomg'ir \U00002614",
        "Thunderstorm" : "Momaqaldiroq \U000026A1",
        "Snow" : "Qor \U0001F328",
        "Mist": "Tumanli \U0001F328",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Derazadan qarang, qanday ob-havo bo'layotganini tushinib bo'lmayapti!"


        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\n"
              f"Kiritilgan shahar: {city}\nTemperatura: {cur_weather}C° {wd}\n"
              f"Havoning namligi: {humidity}%\nHavo bosimi: {pressure} mmHg\nShamol tezligi: {wind} m/s\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\nQuyosh botishi: {sunset_timestamp}\nKunning uzunligi: {length_of_the_day}\n"
              f"***Hayrli kun!***")

    except:
        await message.reply("\U00002620 Shahar nomini tekshirish \U00002620")




if __name__ == "__main__":
    executor.start_polling(dp)