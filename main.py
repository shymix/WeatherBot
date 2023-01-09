import telebot
import requests
import json
import side_info

bot = telebot.TeleBot('5961196532:AAEiw3GGnrU1HB58ZqNu0juBSlqFFnLmsek')


def get_weather():

    city_weather = {}

    def find_weather(city):

        if city in city_weather:
            return city_weather[city]

        api_url = 'https://api.openweathermap.org/data/2.5/weather'
        request = requests.post(url=api_url, params={'q': city, 'APPID': '599d78f146c2112ff090659d29ea9f35', 'units': 'metric'})

        if request.status_code == 200:
            response = json.loads(request.content)
            info = side_info.Weather(response['main']['temp'], response['main']['feels_like'], response['main']['humidity'], response['wind']['speed'])
            city_weather[city] = info
            return city_weather[city]
        return f'I was not able to get the temperature('
    return find_weather


def bra(line):
    list = []
    help =''
    for i in line:
        if i in side_info.punctuation:
            list.append(help)
            help = ''
        else:
            help = help + i
            help = help.strip()
    list.append(help)
    return list


@bot.message_handler(commands=['start'])
#function for /start
def start(message):
    mess = f'{message.from_user.first_name}'
    if message.from_user.last_name:
           mess = mess + message.from_user.last_name
    bot.send_message(message.chat.id, f'Hello {mess}! This shit is actually working')


#function for /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'This bot can bla-bla-bla')


@bot.message_handler(commands=['weather'])
#function for /start
def weather(message):
    bot.send_message(message.chat.id, 'Tell me the city')
    city = input()
    city_weather = {}
    def find():
        pass
    bot.send_message(message.chat.id, city)


@bot.message_handler(func=lambda m: True)
#function for regular messages not with /
def echo_all(message):
    if message.text in side_info.questions:
        bot.send_message(message.chat.id, side_info.questions[message.text])
        breakpoint()
    list_of_cities = bra(message.text)
    print(list_of_cities)
    for i in list_of_cities:
        weather = get_weather()
        bot.reply_to(message, f'{i}:{weather(i)}')


bot.infinity_polling()
