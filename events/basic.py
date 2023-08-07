from line_bot_api import *

def about_us_event(event):
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