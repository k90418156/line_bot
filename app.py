#載入linebot 所需套件
from line_bot_api import*
from events.basic import *

app=Flask(__name__)



#放上Channel Access Token
line_bot_api=LineBotApi('AR/utgr4xRLzLUUYQYSEB/plhtohmsOE6hVULRCT2gI1xEfca5NMDcTg8Jju/MDQpIFYdtILBi20/dzinmUwFmvkJdn9V4FH9St0jC7hK7QHXY80Batr/VcpGKN6qjuhZ7NWFcQbUuzzMGR4q5NPwQdB04t89/1O/w1cDnyilFU=')
#放上Channel Secret
handler=WebhookHandler('febd3d54430c1108648605d77e4e7a5c')

#監聽所有來自/callback 的post Request
@app.route('/callback',methods=['POST'])
def callback():

    #get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']

    #get request body as text
    body=request.get_data(as_text=True)
    app.logger.info('Request body: '+body)

    #handle webhook body
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)

    return 'Ok'

#處理訊息
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    # message=TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token,message)
    message_text=str(event.message.text).lower()

    if message_text=='@使用說明':
        about_us_event(event)
        Usage(event)

    if __name__=='__main__':
        app.run()