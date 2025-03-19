# coding:utf-8
import requests

#スマートフォンで設定したwio nodeのトークンを入れる
url01 = "アクセストークン１"

#request関数を使ってデータを取得する
json1 = requests.get(url01).json()

#"temperature"のデータが取れたときにdataに温度を入れる
data1 = json1["temperature"]

#Discord Bot API の設定
#BOTのトークンとチャンネルID（通知先に応じて変更すること）
DISCORD_TOKEN = 'DiscordのBOTのTOKENを入れてください'  # Discord Bot のトークン
CHANNEL_ID = '送信するDiscordのチャンネルIDを入れてください'  # 送信先のチャンネル ID
url99 = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"#DiscordのWeb APIサーバ
#高温用メッセージ
message1 = '@everyone\n'#@everyoneをつけると通知音が鳴ります
message1+= '高温注意！:'+str(data1)+'℃'
payload1 = {'content' : message1}

#低温用メッセージ
message2 = '@everyone\n'#@everyoneをつけると通知音が鳴ります
message2+= '低温注意！:'+str(data1)+'℃'
payload2 = {'content' : message2}

headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}

#警報を出したいときの温度を設定する
if data1 > 20.0:#高温用：この温度より「高い」と通知する
    r = requests.post(url99,data=payload1,headers=headers)

if data1 < 10.0:#低温用：この温度より「低い」と通知する
    r = requests.post(url99,data=payload2,headers=headers)

"""
本プログラムは β 版です。ご使用になられる環境での動作保証は致しておりません。
Discordでデータ通知を行う際に通知音を鳴らすには「@everyone」をつけてください
"""
