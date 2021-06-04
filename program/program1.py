# coding:utf-8
import requests

#スマートフォンで設定したwio nodeのトークンを入れる
url01 = "アクセストークン１"
url02 = "アクセストークン２"

#request関数を使ってデータを取得する
json1 = requests.get(url01).json()
json2 = requests.get(url02).json()

#エラー判定　jsonのkeyにerrorが含まれていれば「エラー」を返す
#別のセンサを使うときはセンサに応じた"analog"などのKeyを書く
data1 = 'エラー' if ("error" in json1) else json1["temperature"]
data2 = 'エラー' if ("error" in json2) else json2["temperature"]

#LINE notify のURL
#LINE notify のトークン（通知先に応じて変更すること）
    
url99 = "https://notify-api.line.me/api/notify"
token = '通知するLINEグループのアクセストークン'

#LINEに通知するメッセージを記入 ''は文字列のこと
message  = 'ハウスの情報\n'
#message += を使うと通知メッセージを増やせる
#センサ名、データ番号、単位を書く
message += '温度１:'+str(data1)+'℃'+'\n'
message += '温度２:'+str(data2)+'℃'

#LINEに通知するための３行
payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token,}
r = requests.post(url99,data=payload,headers=headers)

"""
本プログラムはβ版です。
Python3.7.3、Numpy1.20.1、Pandas1.2.2、Matplotlib3.3.4で動作確認しておりますが、
ご使用になられる環境での動作保証は致しておりません。
"""