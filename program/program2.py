# coding:utf-8
import requests

#スマートフォンで設定したwio nodeのトークンを入れる
url01 = "アクセストークン１"

#request関数を使ってデータを取得する
json1 = requests.get(url01).json()

#"temperature"のデータが取れたときにdataに温度を入れる
data1 = json1["temperature"]

#LINE notify のURL
#LINE notify のトークン（通知先に応じて変更すること）
url99 = "https://notify-api.line.me/api/notify"
token = '通知するLINEグループのアクセストークン'

#高温用メッセージ
message1 = '高温注意！:'+str(data1)+'℃'
payload1 = {'message' : message1}

#低温用メッセージ
message2 = '低温注意！:'+str(data1)+'℃'
payload2 = {'message' : message2}

headers = {'Authorization' : 'Bearer '+ token,}

#警報を出したいときの温度を設定する
if data1 > 20.0:#高温用：この温度より「高い」と通知する
    r = requests.post(url99,data=payload1,headers=headers)

if data1 < 10.0:#低温用：この温度より「低い」と通知する
    r = requests.post(url99,data=payload2,headers=headers)

"""
本プログラムはβ版です。
Python3.7.3、Numpy1.20.1、Pandas1.2.2、Matplotlib3.3.4で動作確認しておりますが、
ご使用になられる環境での動作保証は致しておりません。
"""