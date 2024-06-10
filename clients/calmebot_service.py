import requests

class CallMeBot:
    
    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = 'sua_api_key'

    def send_message(self, message):
        response = requests.get(
            url = f'{self.__base_url}?phone=+55758888888&text={message}&apikey={self.__api_key}'
        )
        return response.text

# site usado para api do call me bot "https://www.callmebot.com/blog/free-api-whatsapp-messages/"
# coloque sua api key com base nos dados do site
# troque o telefone na linha 11 para seu numero
