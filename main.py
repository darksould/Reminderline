from ParseWeb import Client
from BotLine import Comunication

client = Client()
book = client.main('https://www.packtpub.com/packt/offers/free-learning/')
comu = Comunication()
comu.sendMessage(book, 'https://www.packtpub.com')
