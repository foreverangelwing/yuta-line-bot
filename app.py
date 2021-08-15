#yuta_line_bot
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('XsSSHql8+UwpGf8t9oOakzHFCGisiG1eOrabQAAF6EuqRvgrBWJZTOTDLt7hvKy47RDO4lqM93bSDbWGEuLW2/kVJCDNIgzs+YZVFVMRk/iUtuK7DSUp+3T5hn7yT/xpD42ljNJ+PstPIEot9r+IiAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('88fa68e35b392d71f2f478b8077f0d01')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    pd = {
    'UR-515':'https://bit.ly/3fEkpIw', 'UR-870':'https://bit.ly/3CscGqH', 'AE-300':'https://bit.ly/3Am7SBy', 'M-828':'https://bit.ly/3lLb6us'
    }
    msg = event.message.text
    msg = msg.upper()

    r = '很抱歉，我不懂您在說什麼？\n我有查詢目錄功能...輸入目錄\n單項說明書功能...\業務聯絡資訊\n留言等真人跟您回覆'

    if msg in pd:
        if 'UR' in msg:
            r = msg + '  雙液型壓克力樹脂' +'\n' + '產品說明書(TDS)' + '\n' + pd[msg]
        elif 'AE' in msg:
            r = msg + '  乳化型壓克力樹脂' +'\n' + '產品說明書(TDS)' + '\n' + pd[msg]
        elif 'M' in msg:
            r = msg + '  氨基樹脂' +'\n' + '產品說明書(TDS)' + '\n' + pd[msg]

       
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=r))

        
    
    if msg in ['感謝', '謝謝', '掰掰', 'Ths', '3q', 'Thanks', 'THS', '3Q', 'THANKS']:
        sticker_message = StickerSendMessage(
        package_id='446',
        sticker_id='1993'
    )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return

    if msg in ['hi', 'HI', 'Hi', '你好', '嗨', '哈囉', '你在嗎？', '有人在嗎？']:
        r = '你好！'
    elif msg in ['優達', '優達樹脂', '優達在哪裡?', '優達公司在哪', '總公司']:
        r = '優達樹脂化工股份有限公司\n統編：72177977\n地址：737台南市鹽水區自立街1號（新營工業區）\n網址：https://www.yutar.com/\nTEL：06-6532-110、0905-721-977\nFAX：06-6530-941\n郵箱: service@yutar.com (請在郵件主旨前加『6530941』，以確使您的郵件不會淹沒在Junk mails中！)'
    elif msg in ['優達規模', '公司規模', '生產產品種類', '關於優達']:
        r = '創立於：1980-08-02\n統一編號：72177977\n資本總額：US＄10 Million\n工作夥伴:100\n工廠面積：16500 m²\n新營廠、官田廠\n產品:丙烯酸樹脂、專業的16項產業線胺基樹脂'
    elif msg in ['目錄', '產品需求', '需求', '產品目錄']:
        r = '產品目錄：https://bit.ly/3AljGUx'
    elif '汽車修補' in msg:
        r = '請參照35～36頁\n''產品目錄：https://bit.ly/3AljGUx'
    elif msg in ['北區業務', '業務北區','北區']:
        r = '北區業務：許育愷 主任\n電話：0937815151\nEmail:kyra@yutar.com'
    elif msg in ['中區業務', '業務中區', '中區']:
        r = '中區業務：蔡家純 主任\n聯繫方式：020479979'
    elif msg in ['南區業務', '業務南區', '南區']:
        r = '南區業務：郭明豐 經理\n聯絡方式：094879487'
    elif '業務人員' in msg:
        r = '您可以在對話視窗輸入"XX業務"即可查詢聯繫資料\n例如：北區業務、中區業務、南區業務'
    elif '業務' in msg:
        r = '您可以在對話視窗輸入"XX業務"即可查詢聯繫資料\n例如：北區業務、中區業務、南區業務'


        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    


if __name__ == "__main__":
    app.run()