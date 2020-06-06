from datetime import datetime

index = [
    'current',
    'after6Hours',
    'after12Hours',
    'after15Hours',
    'day'
]

def filterApiInfo(content):
    contentFiltered = {
        'current': {
            'temp': content['current']['temp'],
            'feelsLike': content['current']['feels_like'],
            'humidity': content['current']['humidity'],
            'windSpeed': content['current']['wind_speed'],
            'clouds': content['current']['clouds'],
            'sky': content['current']['weather'][0]['main'],
            'skyDescription': content['current']['weather'][0]['description']
        },
        'after6Hours': {
            'temp': content['hourly'][5]['temp'],
            'feelsLike': content['hourly'][5]['feels_like'],
            'humidity': content['hourly'][5]['humidity'],
            'windSpeed': content['hourly'][5]['wind_speed'],
            'clouds': content['hourly'][5]['clouds'],
            'sky': content['hourly'][5]['weather'][0]['main'],
            'skyDescription': content['hourly'][5]['weather'][0]['description']
        },
        'after12Hours': {
            'temp': content['hourly'][11]['temp'],
            'feelsLike': content['hourly'][11]['feels_like'],
            'humidity': content['hourly'][11]['humidity'],
            'windSpeed': content['hourly'][11]['wind_speed'],
            'clouds': content['hourly'][11]['clouds'],
            'sky': content['hourly'][11]['weather'][0]['main'],
            'skyDescription': content['hourly'][11]['weather'][0]['description']
        },
        'after15Hours': {
            'temp': content['hourly'][14]['temp'],
            'feelsLike': content['hourly'][14]['feels_like'],
            'humidity': content['hourly'][14]['humidity'],
            'windSpeed': content['hourly'][14]['wind_speed'],
            'clouds': content['hourly'][14]['clouds'],
            'sky': content['hourly'][14]['weather'][0]['main'],
            'skyDescription': content['hourly'][14]['weather'][0]['description']
        },
        'day': {
            'min': content['daily'][0]['temp']['min'],
            'max': content['daily'][0]['temp']['max'],
            'dayTemp': content['daily'][0]['temp']['day'],
            'nightTemp': content['daily'][0]['temp']['night'],
            'clouds': content['daily'][0]['clouds'],
            'sky': content['daily'][0]['weather'][0]['main'],
            'skyDescription': content['daily'][0]['weather'][0]['description']
        }
    }
    if contentFiltered['day']['sky'] == 'Rain': contentFiltered['day']['rain'] = content['daily'][0]['rain']
    return contentFiltered

def arrangeSky(content):
    sky = {}

    for items in index:
        if content[items]['sky'] == 'Clouds': sky[items] = 'com nuvens!'
        elif content[items]['sky'] == 'Clear': sky[items] = 'aberto!'
        elif content[items]['sky'] == 'Rain': sky[items] = 'com probabilidade de Chuva!'
    return sky

def generateText(apiContent, sky):
    texts = {}

    for items in index:
        if items == 'day': break
        texts[items] = f'''
            Temperatura: {apiContent[items]['temp']}C°
            Sensação Térmica: {apiContent[items]['feelsLike']}C°
            Umidade: {apiContent[items]['humidity']}%
            Velocidade do Vento: {apiContent[items]['windSpeed']}m/s
            Nuvens: {apiContent[items]['clouds']}%

            O tempo estará {sky[items]}
        '''
    return texts

def generateProbRain(apiContent):
    for i in apiContent['day']:
        if i == 'rain':
            return (apiContent['day']['rain'] / 24) * 100
        else: continue
    else: return 0

def setCorrectHour(hour):
    if hour < 24: return hour
    else: return hour - 24

def generateEmail(apiContent, mailTo = False):
    today = str(datetime.now().today())[:9]
    hour = datetime.now().hour
    minute = datetime.now().minute
    after6 = setCorrectHour(hour + 6)
    after12 = setCorrectHour(hour + 12)
    after15 = setCorrectHour(hour + 15)
    sky = arrangeSky(apiContent)
    line = '-'*60
    texts = generateText(apiContent, sky)
    probRain = generateProbRain(apiContent)
    
    email = {
        'mailTo': mailTo,
        'subject': f'Previsão do Tempo para: {today}',
        'message': f'''
            Olá, Vamos à Previsão do Tempo!

            Neste exato momento: {hour}:{minute} -

            {texts['current']}

            {line}

            Às {after6}:{minute} estará - 

            {texts['after6Hours']}

            {line}

            Às {after12}:{minute} estará - 

            {texts['after12Hours']}

            {line}

            Às {after15}:{minute} estará - 

            {texts['after15Hours']}

            {line}

            Ao resumo do dia - 

            A mínima será de: {apiContent['day']['min']}C°
            A máxima será de: {apiContent['day']['max']}C°
            Temperatura média durante o dia: {apiContent['day']['dayTemp']}C°
            Temperatura média durante a noite: {apiContent['day']['nightTemp']}C°
            Nuvens: {apiContent['day']['clouds']}%

            O tempo estará {sky['day']}
            Probabilidade de chuva: {probRain}%

            {line}
        '''
    }

    return email
