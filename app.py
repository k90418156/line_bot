#載入linebot 所需套件
from flask import Flask,request,abort
from linebot import (LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*

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
    emoji = [
        {
        'index':0,
        'productId':'5ac1bfd5040ab15980c9b435',
        'emojiId':'001'
    },
    {
        'index':17,
        'productId':'5ac1bfd5040ab15980c9b435',
        'emojiID':'001'
    }
    ]
    text_message=TextSendMessage(text='''$ Master Finance $
Hello!您好，還營您成為Master Finance的好友!
                                 
我是Master 財經小幫手
這裡有股票，匯率資訊
直接點選下方選單
''',emojis=emoji)
    sticker_message=StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,sticker_message])

    if __name__=='__main__':
        app.run()