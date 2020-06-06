class EmailValidation:
    def __init__(self):
        self.name = 'EmailBot'

    def validateInput(self, mailTo, subject, message):
        if not mailTo or not subject or not message:
            raise Exception(f'[On {self.name}] all the params are required')
        elif type(mailTo) != str:
            raise Exception(f'[On {self.name}] Invalid type for "mailTo":{type(mailTo)}, need to be {str}')
        elif type(subject) != str:
            raise Exception(f'[On {self.name}] Invalid type for "subject":{type(subject)}, need to be {str}')
        elif type(message) != str:
            raise Exception(f'[On {self.name}] Invalid type for "message":{type(message)}, need to be {str}')

    def validateTimeInput(self, hour, minute):
        if type(hour) != int:
            raise Exception(f'[On {self.name}] Invalid type for "hour":{type(hour)}, need to be {int}')
        elif type(minute) != int:
            raise Exception(f'[On {self.name}] Invalid type for "minute":{type(minute)}, need to be {int}')

class WeatherValidation:
    def __init__(self):
        self.name = 'WeatherBot'

    def validateInput(self, cityCoords, apiKey, units):
        if not cityCoords or not apiKey:
            raise Exception(f'[On {self.name}] all the params are required')
        elif type(cityCoords) != list:
            raise Exception(f'[On {self.name}] Invalid type for "cityCoords":{type(cityCoords)}, need to be {list}')
        elif type(apiKey) != str:
            raise Exception(f'[On {self.name}] Invalid type for "apiKey":{type(apiKey)}, need to be {str}')
        elif type(units) != str:
            raise Exception(f'[On {self.name}] Invalid type for "units":{type(units)}, need to be {str}')
    
    def validateContent(self, content):
        if not content:
            raise Exception(f'[On {self.name}] all the params are required')
        elif type(content) != dict:
            raise Exception(f'[On {self.name}] Invalid type for "content":{type(content)}, need to be {dict}')