punctuation = ['.', ',', ';', '!', '?']

questions = {
    "How are you?": "I'm fine thanks)",
    "2+2": "4",
}

class Weather:

     def __init__(self, temp, feels_like, humidity, wind_speed):
         self.temp = temp
         self.feels_like = feels_like
         self.humidity = humidity
         self.wind_speed = wind_speed


     def __str__(self):
        return f'temperature:{self.temp}, feels like:{self.feels_like}, humidity:{self.humidity}, wind speed:{self.wind_speed}'