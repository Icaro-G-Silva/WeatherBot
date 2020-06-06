# Weather-Bot
> Basic weather bot with precious information about climate

# How does it work?
It's very simple because it uses only two APIs to work:
+ openWeather
+ SMTP (Email)

with **openWeather** we can catch some informations about the weather and then, with **SMTP** we send that information to someone's email.
Particularly in this bot, we can also set a specific time to send the weather's infos.

# Functionalities
  + Get information about the weather in a specific region around the world
  + Send by email the informations about the weather we got before
  + Set a specific time to send the email

# Comments
For everything to work correctly you need some email to do the sending part, so in the **.json** file you need to put the email address and the email password.
Also in the main file on calling the constructor "ForecastBot" you need to specify the coordinates to your city or neighborhood etc... for that you just need to pass an list with the latitude and longitude.
For example: `ForecastBot(cityCoords = [lat,long], mailTo = email)`

# Version
> 1.0
