from flask import Flask, request, abort,jsonify
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage)
from  flask.ext.pymongo import  PyMongo
#import datetime
#import time
app = Flask(__name__)


line_bot_api = LineBotApi('iYDoDLW1k4yIYJvMnHVi18Vhl0NXPh5ec6a4FLdlR/en3nqmGCWsF/QeYKX8MPj2DYUFbjsEos/+HGUA7LgF4OimIUh1WD9j/phhG/vqX9zZD92iiw/t+kpE1AadWCIdwkzMuxEvAbCM84LtdTkQSgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('935cecc6bf121cf08c1cea288956462b')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

        if event.message.text == 'รูป':
            image_message = ImageSendMessage(
                original_content_url='https://raw.githubusercontent.com/kittinan/Sample-Line-Bot/master/images/beer.jpg',
                preview_image_url='https://raw.githubusercontent.com/kittinan/Sample-Line-Bot/master/images/beer.jpg'
            )
            line_bot_api.reply_message(event.reply_token, TextSendMessage(image_message))


if __name__ == '__main__':
    app.run()