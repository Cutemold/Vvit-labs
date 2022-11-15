import requests as req  # import module - requests
import datetime  # import module - datetime for daily weather

# Initialize new variables with APP-ID and required city

city = "Moscow,RU"
appid = "f5fa7ad3e26f06d0db0f02869d71f6b7"

# Creating a request to receive information from the service

res = req.get("http://api.openweathermap.org/data/2.5/weather", params={'q':city, 'units':'metric', 'lang':'ru', 'APPID':appid})
data = res.json()
now = datetime.datetime.now()
# Daily weather
print("================================")
print("День: <", str(now.year) + '-' + str(now.month) + '-' + str(now.day), '>')
print("Город:", city)
print("Погодные условия:", data["weather"][0]["description"])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
print("================================")

#Домашнее задание:
res = req.get("http://api.openweathermap.org/data/2.5/forecast", params={'q':city, 'units':'metric', 'lang':'ru', 'APPID':appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата: <", i['dt_txt'], ">, \r\nСкорость ветра: <", i['wind']['speed'], ">", "\r\nВидимость: <", i['visibility'], ">")
    print("________________________________")