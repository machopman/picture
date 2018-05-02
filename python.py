from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage,
                            CarouselTemplate, CarouselColumn, PostbackTemplateAction, MessageTemplateAction,
                            URITemplateAction)

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
                original_content_url='https://imagemovie.herokuapp.com/pic1.jpg',
                preview_image_url='https://imagemovie.herokuapp.com/pic1.jpg'
            )
            line_bot_api.push_message('U7183997e3e85a10d8c5f1f3925825016', image_message)

        if event.message.text=='ปุ่ม':
            message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://imagemovie.herokuapp.com/tt3501632.jpg',
                            title='this is menu1',
                            text='description1',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback1',
                                    text='postback text1',
                                    data='action=buy&itemid=1'
                                ),
                                MessageTemplateAction(
                                    label='message1',
                                    text='message text1'
                                ),
                                URITemplateAction(
                                    label='uri1',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://imagemovie.herokuapp.com/tt3501632.jpg',
                            title='this is menu2',
                            text='description2',
                            actions=[
                                PostbackTemplateAction(
                                    label='postback2',
                                    text='postback text2',
                                    data='action=buy&itemid=2'
                                ),
                                MessageTemplateAction(
                                    label='message2',
                                    text='message text2'
                                ),
                                URITemplateAction(
                                    label='uri2',
                                    uri='http://mandm.plearnjai.com/'
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)



if __name__ == '__main__':
    app.run()