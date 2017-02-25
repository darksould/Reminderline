from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

class Comunication(object):

    def sendMessage(self, message, site):
        line_bot_api = LineBotApi('l6NTh6EYXE766wlDP0VH8rnCq6xaKdVDEz/ftsvNRUTIAdsN1TLZICqglf1ZirJWHZFGACxJSId31uB8evc63bdgDyvYeSOdLAU5CtXguPmyREgM6MlgEUtx52U60D69CsxyGDWRhGrXTc//onIE6gdB04t89/1O/w1cDnyilFU=')
        try:
            line_bot_api.push_message('U812248f1178cc8f3ab090cae98a28a29', TextSendMessage(text='There is a new book that you can download from '+site+ ' - '+message))
        except LineBotApiError as e:
            print 'The message could not be sent'
