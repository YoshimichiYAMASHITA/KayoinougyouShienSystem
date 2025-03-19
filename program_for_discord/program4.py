# coding:utf-8
import requests
import os

#スマートフォンで設定したwio nodeのトークンを入れる
url01 = "アクセストークン１"
url02 = "アクセストークン２"
url03 = "アクセストークン３"
url04 = "アクセストークン４"
url05 = "アクセストークン５"
url06 = "アクセストークン６"

#request関数を使ってデータを取得する
json1 = requests.get(url01).json()
json2 = requests.get(url02).json()
json3 = requests.get(url03).json()
json4 = requests.get(url04).json()
json5 = requests.get(url05).json()
json6 = requests.get(url06).json()

#エラー判定　jsonのkeyにエラーが含まれていれば「空白」を返す
#別のセンサを使うときはセンサに応じた"analog"などのKeyを書く
data1 = ' ' if ("error" in json1) else json1["temperature"]
data2 = ' ' if ("error" in json2) else json2["temperature"]
data3 = ' ' if ("error" in json3) else json3["temperature"]
data4 = ' ' if ("error" in json4) else json4["temperature"]
data5 = ' ' if ("error" in json5) else json5["temperature"]
data6 = ' ' if ("error" in json6) else json6["temperature"]

#Discord Bot API の設定
#BOTのトークンとチャンネルID（通知先に応じて変更すること）
DISCORD_TOKEN = 'DiscordのBOTのTOKENを入れてください'  # Discord Bot のトークン
CHANNEL_ID = '送信するDiscordのチャンネルIDを入れてください'  # 送信先のチャンネル ID
url99 = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"#DiscordのWeb APIサーバ

#LINEに通知するメッセージを記入
message  = 'ハウス情報\n'
#'センサ名:'+str(data番号)+'単位'+'\n'　センサ名、データ番号、単位を書く
message += '温度１:'+str(data1)+'単位'+'\n'
message += '温度２:'+str(data2)+'単位'+'\n'
message += '温度３:'+str(data3)+'単位'+'\n'
message += '温度４:'+str(data4)+'単位'+'\n'
message += '温度５:'+str(data5)+'単位'+'\n'
message += '温度６:'+str(data6)+'単位'

payload = {"content": message  } 
headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}

r = requests.post(url99, data=payload, headers=headers)

#csvの保存のために時刻を取得
timestamp = 'date +%F" %H:%M:%S"'
current_time = os.popen(timestamp).readline().strip()

#csvで保存するデータを組み合わせる
data_set  = str(current_time) 
data_set += ',' + str(data1)
data_set += ',' + str(data2)
data_set += ',' + str(data3)
data_set += ',' + str(data4)
data_set += ',' + str(data5)
data_set += ',' + str(data6)
data_set += '\n'

#/home/pi/data.txtというファイルにデータを保存する
fout = open('/home/pi/data.txt','at')
fout.write(data_set)
fout.close()


# メッセージを送信できたかどうかのチェック（トラブル報告用）
if r.status_code == 200 or r.status_code == 201:
    print("メッセージ送信が成功しました")
else:
    print("エラーが発生しました: " + str(r.status_code) + " - " + r.text)

"""
本プログラムは β 版です。ご使用になられる環境での動作保証は致しておりません。
Discordでデータ通知を行う際に通知音を鳴らすには「@everyone」をつけてください
"""
