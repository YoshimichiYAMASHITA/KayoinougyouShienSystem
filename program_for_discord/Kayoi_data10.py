# coding:utf-8
import requests #Web APIにアクセスするために用いる
import time #時刻の取得に用いる
import os #CSVファイルの保存に用いる
from decimal import Decimal, ROUND_HALF_UP #四捨五入に用いる

#スマートフォンで設定したwio nodeのトークンを入れる
#【Wio Node 001】
# 温湿度センサ-温度 key:temperature
url01 = "アクセストークン１"
#"""　
# 温湿度センサ-湿度 key:humidity
url02 = "アクセストークン２"
#【Wio Node 002】
# 温度センサ-地温 key:temperature
url03 = "アクセストークン３"
# 土壌水分センサ-土壌水分 key:moisture
url04 = "アクセストークン４"
#"""

#request関数とfor関数を使って最大3回 5秒おきにデータを取得する
CONNECTION_RETRY = 3 #データ取得を行う最大試行数を設定する
INTERVAL_TIME = 5 #データ取得失敗時に何秒待つかを設定する

#data1（json1の後には設定したセンサにあわせて「keyキー」を記入する）
#1<= X < 4 なので3 回試行する
for i1 in range(1, CONNECTION_RETRY+1):
    json1 = requests.get(url01).json()
    if ("error" in json1) :
        if("Node is offline" in json1["error"]):
            data1 = ' OFF'#マイコンに電源が来ていないかWiFiの電源がオフです
            break
        elif("timeout" in json1["error"]):
            data1 = 'TIME'#マイコン再起動中かWiFiの調子が悪いです
            time.sleep(INTERVAL_TIME)
        elif("METHOD" in json1["error"]):
            data1 = 'FWUP'#Wioアプリでのファームウェアアップデート失敗か、アプリで接続しているセンサが正しいかを確認してください
            break
        elif("Unknown" in json1["error"]):
            data1 = ' UNK'#センサが壊れているか、センサが抜けています。
            time.sleep(INTERVAL_TIME)
        else:
            data1 = 'FAIL'#データ取得に失敗しました。WiFiの電波が弱いか、マイコンの調子が悪いかもしれません。
            time.sleep(INTERVAL_TIME)
    else:
        data1 = (Decimal(json1["temperature"]).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))#データを四捨五入します
        break

#"""
for i2 in range(1, CONNECTION_RETRY+1):
    json2 = requests.get(url02).json()
    if ("error" in json2) :
        if("Node is offline" in json2["error"]):
            data2 = ' OFF'#マイコンに電源が来ていないかWiFiの電源がオフです
            break
        elif("timeout" in json2["error"]):
            data2 = 'TIME'#マイコン再起動中かWiFiの調子が悪いです
            time.sleep(INTERVAL_TIME)
        elif("METHOD" in json2["error"]):
            data2 = 'FWUP'#Wioアプリでのファームウェアアップデート失敗か、アプリで接続しているセンサが正しいかを確認してください
            break
        elif("Unknown" in json2["error"]):
            data2 = ' UNK'#センサが壊れているか、センサが抜けています。
            time.sleep(INTERVAL_TIME)
        else:
            data2 = 'FAIL'#データ取得に失敗しました。WiFiの電波が弱いか、マイコンの調子が悪いかもしれません。
            time.sleep(INTERVAL_TIME)
    else:
        data2 = (Decimal(json2["humidity"]).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))#データを四捨五入します
        break

for i3 in range(1, CONNECTION_RETRY+1):
    json3 = requests.get(url03).json()
    if ("error" in json3) :
        if("Node is offline" in json3["error"]):
            data3 = ' OFF'#マイコンに電源が来ていないかWiFiの電源がオフです
            break
        elif("timeout" in json3["error"]):
            data3 = 'TIME'#マイコン再起動中かWiFiの調子が悪いです
            time.sleep(INTERVAL_TIME)
        elif("METHOD" in json3["error"]):
            data3 = 'FWUP'#Wioアプリでのファームウェアアップデート失敗か、アプリで接続しているセンサが正しいかを確認してください
            break
        elif("Unknown" in json3["error"]):
            data3 = ' UNK'#センサが壊れているか、センサが抜けています。
            time.sleep(INTERVAL_TIME)
        else:
            data3 = 'FAIL'#データ取得に失敗しました。WiFiの電波が弱いか、マイコンの調子が悪いかもしれません。
            time.sleep(INTERVAL_TIME)
    else:
        data3 = (Decimal(json3["temperature"]).quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))#データを四捨五入します
        break

for i4 in range(1, CONNECTION_RETRY+1):
    json4 = requests.get(url04).json()
    if ("error" in json4) :
        if("Node is offline" in json4["error"]):
            data4 = ' OFF'#マイコンに電源が来ていないかWiFiの電源がオフです
            break
        elif("timeout" in json4["error"]):
            data4 = 'TIME'#マイコン再起動中かWiFiの調子が悪いです
            time.sleep(INTERVAL_TIME)
        elif("METHOD" in json4["error"]):
            data4 = 'FWUP'#Wioアプリでのファームウェアアップデート失敗か、アプリで接続しているセンサが正しいかを確認してください
            break
        elif("Unknown" in json4["error"]):
            data4 = ' UNK'#センサが壊れているか、センサが抜けています。
            time.sleep(INTERVAL_TIME)
        else:
            data4 = 'FAIL'#データ取得に失敗しました。WiFiの電波が弱いか、マイコンの調子が悪いかもしれません。
            time.sleep(INTERVAL_TIME)
    else:
        data4 = (Decimal(json4["moisture"]).quantize(Decimal('1'),rounding=ROUND_HALF_UP))#データを四捨五入します
        break
#"""
#Discord Bot API の設定
DISCORD_TOKEN = 'DiscordのBOTのTOKENを入れてください'  # Discord Bot のトークン
CHANNEL_ID = '（１）001ハウス情報（定期通知）のトークン'  # 送信先のチャンネル ID
url99 = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"#DiscordのWeb APIサーバ

#"""
#LINEに通知するメッセージを作る
message  = '\n'
#'センサ名:'+str(data番号)+'単位'+'\n'　センサ名、データ番号、単位を書く
message += '■ハウス環境'+'\n'
message += '　　温度:'+str(data1)+'　℃'+'\n'
#"""
message += '　　湿度:'+str(data2)+'　%RH'+'\n'
message += '　　地温:'+str(data3)+'　℃'+'\n'
message += '土壌水分:'+str(data4)+''
#"""

#LINEグループに通知を行う
payload = {"content": message  } 
headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
r = requests.post(url99, data=payload, headers=headers)
#"""

#CSVで保存する
#CSVの保存のために時刻を取得
timestamp = 'date +%F" %H:%M"'
current_time = os.popen(timestamp).readline().strip()
#CSVで保存するデータを組み合わせる
data_set  = str(current_time) 
data_set += ',' + str(data1)
#"""
data_set += ',' + str(data2)
data_set += ',' + str(data3)
data_set += ',' + str(data4)
#"""
data_set += '\n'

#/home/pi/data.txtというファイルにデータを保存する
fout = open('/home/pi/data10.txt','at')
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