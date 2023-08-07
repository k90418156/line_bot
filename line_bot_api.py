#載入linebot 所需套件
from flask import Flask,request,abort
from linebot import (LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*


#放上Channel Access Token
line_bot_api=LineBotApi('AR/utgr4xRLzLUUYQYSEB/plhtohmsOE6hVULRCT2gI1xEfca5NMDcTg8Jju/MDQpIFYdtILBi20/dzinmUwFmvkJdn9V4FH9St0jC7hK7QHXY80Batr/VcpGKN6qjuhZ7NWFcQbUuzzMGR4q5NPwQdB04t89/1O/w1cDnyilFU=')
#放上Channel Secret
handler=WebhookHandler('febd3d54430c1108648605d77e4e7a5c')