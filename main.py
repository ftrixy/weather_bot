import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        temp_min_weather = data["main"]["temp_min"]
        temp_max_weather = data["main"]["temp_max"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Глянь у вікно, я не можу зрозуміти яка там погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"\U0001F4C6 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} \U0000231A\n"
              "\n" 
              f"Погода в місті: {city}\n"
              "\n" 
              f"Температура: {cur_weather}C° {wd}\n"
              f"Максимальна: {temp_max_weather}C°\nМінімальна: {temp_min_weather}C°\n"
              "\n" 
              f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\n"
              f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\nТривалість дня: {length_of_the_day}\n"
              "\n"         
              f"\U00002764 Гарного дня! \U0001F618"
              )

    except Exception as ex:
        print(ex)
        print("Перевірь назву міста")


def main():
    city = input("Напиши назву міста: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()