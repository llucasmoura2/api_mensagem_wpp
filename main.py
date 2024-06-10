from clients.calmebot_service import CallMeBot
from clients.conversor_service import CoinConversorService




conversor_service = CoinConversorService()

conversion =conversor_service.converter('BTC', 'BRL')

wpp_service = CallMeBot()
wpp_service.send_message(
   message= f'cotação do bitcoin: {conversion} R$'
)





