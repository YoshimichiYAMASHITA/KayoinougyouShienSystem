# coding:utf-8
import requests
import time

#スマートフォンで設定したwio nodeのトークンを入れる
url01 = "アクセストークン１"
url02 = "アクセストークン２"
url03 = "アクセストークン３"

#request関数とfor関数を使って最大３回 ５秒おきにデータを取得する
CONNECTION_RETRY = 3
INTERVAL_TIME = 5

#data1
#1<= X < 4 なので1 2 3 回試行する
for i1 in range(1, CONNECTION_RETRY+1):
    json1 = requests.get(url01).json()
    if ("error" in json1) :
        data1 = 'エラー'
        print('data 1 error!')
        time.sleep(INTERVAL_TIME)
    else:
        data1 = json1["temperature"]
        break

#data2
for i2 in range(1, CONNECTION_RETRY+1):
    json2 = requests.get(url02).json()
    if ("error" in json2) :
        data2 = 'エラー'
        print('data 2 error!')
        time.sleep(INTERVAL_TIME)
    else:
        data2 = json2["temperature"]
        break

#data3
for i3 in range(1, CONNECTION_RETRY+1):
    json3 = requests.get(url03).json()
    if ("error" in json3) :
        data3 = 'エラー'
        print('data 3 error!')
        time.sleep(INTERVAL_TIME)
    else:
        data3 = json3["temperature"]
        break

#Discord Bot API の設定
#BOTのトークンとチャンネルID（通知先に応じて変更すること）
DISCORD_TOKEN = 'DiscordのBOTのTOKENを入れてください'  # Discord Bot のトークン
CHANNEL_ID = '送信するDiscordのチャンネルIDを入れてください'  # 送信先のチャンネル ID
url99 = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"#DiscordのWeb APIサーバ

#LINEに通知するメッセージを記入
message  = 'ハウス情報\n'
#'センサ名:'+str(data番号)+'単位'+'\n'　センサ名、データ番号、単位を書く
message += '温度１:'+str(data1)+'℃'+'\n'
message += '温度２:'+str(data2)+'℃'+'\n'
message += '温度３:'+str(data3)+'℃'
#必要に応じて接続回数を通知する
message += '\n'+'接続回数:'+str(i1)+' '+str(i2)+' '+str(i3)

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
"""
