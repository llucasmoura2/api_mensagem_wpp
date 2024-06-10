import requests

class CallMeBot:
    
    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = '9771278'

    def send_message(self, message):
        response = requests.get(
            url = f'{self.__base_url}?phone=+557192209258&text={message}&apikey={self.__api_key}'
        )
        return response.text
