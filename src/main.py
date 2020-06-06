from forecastBot import ForecastBot

bot = ForecastBot(mailTo = 'email@gmail.com')
bot.scheduleTime(hour = 6)
bot.sendWeatherForecast()
