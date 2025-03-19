# coding:utf-8
import requests

# スマートフォンで設定した Wio Node のトークンを入れる
url01 = "アクセストークン１"
url02 = "アクセストークン２"

# request 関数を使ってデータを取得する
json1 = requests.get(url01).json()
json2 = requests.get(url02).json()

# エラー判定 json の key に error が含まれていれば「エラー」を返す
# 別のセンサを使うときはセンサに応じた "analog" などの Key を書く
data1 = 'エラー' if ("error" in json1) else json1["temperature"]
data2 = 'エラー' if ("error" in json2) else json2["temperature"]

#Discord Bot API の設定
#BOTのトークンとチャンネルID（通知先に応じて変更すること）
DISCORD_TOKEN = 'DiscordのBOTのTOKENを入れてください'  # Discord Bot のトークン
CHANNEL_ID = '送信するDiscordのチャンネルIDを入れてください'  # 送信先のチャンネル ID
url99 = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"#DiscordのWeb APIサーバ

#Discordに通知するメッセージを記入 ''は文字列のこと
message  = 'ハウスの情報\n'
#message += を使うと通知メッセージを増やせる
#センサ名、データ番号、単位を書く
message += '温度１:'+str(data1)+'℃'+'\n'
message += '温度２:'+str(data2)+'℃'

#Discordに通知するための３行(LINE Notifyと異なり、messageはcontentで送ります)
payload = {"content": message  } 
headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
r = requests.post(url99, data=payload, headers=headers)


# メッセージを送信できたかどうかのチェック（トラブル報告用）
if r.status_code == 200 or r.status_code == 201:
    print("メッセージ送信が成功しました")
else:
    print("エラーが発生しました: " + str(r.status_code) + " - " + r.text)

"""
本プログラムは β 版です。ご使用になられる環境での動作保証は致しておりません。
Discordでデータ通知を行う際に通知音を鳴らすには「@everyone」をつけてください
通知音を鳴らす場合は24行目から28行目を以下のように書き変えてください。
message  = '@everyone\n'#@everyoneをつけると通知音が鳴ります
message += 'ハウスの情報\n'
#message += を使うと通知メッセージを増やせる
#センサ名、データ番号、単位を書く
message += '温度１:'+str(data1)+'℃'+'\n'
message += '温度２:'+str(data2)+'℃'
"""
