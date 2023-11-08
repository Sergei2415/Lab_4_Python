import json
import requests
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

TokenFB = '6940757048:AAGbsleJvCmsi0aNGhTSs-7gX66TfEMi32w'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Напиши мне название города, а я выдам тебе прогноз погоды на 7 дней.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    index = 0
    day_weather = ""
    time_of_day = ["Утро", "День", "Вечер", "Ночь"]
    try:
        response_coordinates = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + update.message.text + "&count=1&language=ru&format=json")  
        response_weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(json.loads(response_coordinates.text)["results"][0]["latitude"]) + "&longitude=" + str(json.loads(response_coordinates.text)["results"][0]["longitude"]) + "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
        response_weather = response_weather.json()
        for i in range(7):
            index += 12
            day_weather += "Прогноз погоды на " + str(response_weather["hourly"]["time"][index])[5:-6] + "\n"
            for j in range(4):
                day_weather += "" + time_of_day[j] + "\n"
                day_weather += "Температура - " + str(response_weather["hourly"]["temperature_2m"][index]) + "°С\n"
                day_weather += "Влажность - " + str(response_weather["hourly"]["relative_humidity_2m"][index]) + "%\n"
                day_weather += "Скорость ветра - " + str(response_weather["hourly"]["wind_speed_10m"][index]) + "м/c\n"
                index += 3
            await context.bot.send_message(chat_id=update.effective_chat.id, text=day_weather)
            day_weather = ""
    except Exception:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Некорректно введен город! Повторите попытку.")



if __name__ == '__main__':
    application = ApplicationBuilder().token(TokenFB).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    application.run_polling()