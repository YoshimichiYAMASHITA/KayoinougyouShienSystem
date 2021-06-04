# coding: utf-8
import pandas as pd #pandasをインポートする
import matplotlib.pyplot as plt #グラフを描画するのに用いる
import matplotlib as mpl #フォント名を指定するためにインポート
from datetime import date,timedelta #日付を扱うための標準ライブラリ
import requests
import datetime
from decimal import Decimal, ROUND_HALF_UP #四捨五入に用いる

# 読み込むcsvファイル名（絶対パスを推奨）
csv_file = "/home/pi/data10.txt"

# data10.txtにはヘッダーが無いので、列に名前をつける.
col01 = "温度"
#"""
col02 = "湿度"
col03 = "地温"
col04 = "土壌水分"
#"""
colums_name = ["datetime"]
colums_name.append(col01)
#"""
colums_name.append(col02)
colums_name.append(col03)
colums_name.append(col04)
#"""

# csv_fileをデータフレーム型で読み込む
df = pd.read_csv(csv_file, names = (colums_name),  index_col = "datetime", parse_dates = True, encoding = "UTF8")

# データが取れなかった場合の警告があるところをNaNにする
df = df.replace(' OFF', 'NaN')
df = df.replace('TIME', 'NaN')
df = df.replace('FWUP', 'NaN')
df = df.replace(' UNK', 'NaN')
df = df.replace('FAIL', 'NaN')
# NaNを含む行を除外する
df = df.dropna(how = "any")
# データが文字列になっているのでfloatに変更
df = df.astype(float)

# 基準日を算出する（通常はプログラム実行日）
d = datetime.date.today()
# 日時を指定する方法
#d = date(2020,12,30)

# 【基準日を含めた合計48時間を出力する】
d1 = d + timedelta(days = -1)# 基準日の前日を算出する
d2 = d + timedelta(days = +1)# 基準日の翌日を算出する

#matplotlibのフォントを日本語にする
mpl.rcParams['font.family'] = "Noto Sans CJK JP"

#全ての項目をグラフ化＆画像として保存
#グラフ１：ハウス温度（1つのグラフで）
df.plot.line( y = ["温度"], subplots = False, grid = True, figsize=(8,8), xlim = [d1,d2], ylim = [0,40], colormap = "Set1")
plt.savefig("graph1.png")

#"""
#グラフ２：ハウス湿度（1つのグラフで）
df.plot.line( y = ["湿度"], subplots = False, grid = True, figsize=(8,8), xlim = [d1,d2], ylim = [0,100], colormap = "Set1")
plt.savefig("graph2.png")

#グラフ３：地温（1つのグラフで）
df.plot.line( y = ["地温"], subplots = False, grid = True, figsize=(8,8), xlim = [d1,d2], ylim = [0,40], colormap = "Set1")
plt.savefig("graph3.png")

#グラフ４：土壌水分（1つのグラフで）
df.plot.line( y = ["土壌水分"], subplots = False, grid = True, figsize=(8,8), xlim = [d1,d2], ylim = [0,1023], colormap = "Set1")
plt.savefig("graph4.png")

#グラフ5：ハウス温度、ハウス湿度、地温、土壌水分（それぞれのグラフを1枚で）
df.plot.line( y = ["温度","湿度","地温","土壌水分"], subplots = True, grid = True, figsize=(8,8), xlim = [d1,d2], colormap = "Set1")
plt.savefig("graph5.png")

#グラフ6：ハウス温度、地温（１つのグラフで）
df.plot.line( y = ["温度","地温"], subplots = False, grid = True, figsize=(8,8), xlim = [d1,d2], ylim = [0,40], colormap = "Set1")
plt.savefig("graph6.png")
#"""

# DatetimeIndexの秒を切り捨て　floor
print(df.index)
df.index = df.index.floor("min")
print(df.index)

# 【統計量を計算する（通知日から基準日までの区間）】
d_td = d 
d_ld = d_td + timedelta(days = -1   ) # 基準日（通知日1日前とする）

# df.indexの中身はtimestamp型であり、通知日で設定したdate型との比較では怒られるので、timestamp型に変換する
d_td = pd.to_datetime(d_td)
d_ld = pd.to_datetime(d_ld)

#【統計量を計算する】
#平均、最高、最低を算出する。日平均気温は1時～24時までの毎正時の平均値なので、60minデータをdf3とする
#24時（00:00:00）のデータを計算に入れるために全体を10分前にずらす（8/10 00:00:00 -> 8/9 23:50:00）
df2 = df
df3 = df
df2= df[(df.index >= d_ld) & (df.index <= d_td)]
df2.index = df2.index + timedelta(minutes = -10)

# 指定した範囲でdfを抽出（置換）
df2= df2[(df2.index >= d_ld) & (df2.index <= d_td)]#10minずらしたことで出てくる前後+1日を削除
# 10分データから最大値・最小値を算出する
df_max = df2.resample("1D").max()
df_min = df2.resample("1D").min()

#【平均値を算出するために60minデータを作成する】
df3 = df[(df.index >= d_ld) & (df.index <= d_td)]
df3 = df3.asfreq('1H') #60minデータを作成
# 全体を1時間前にずらす（例：8/10 00:00:00 -> 8/9 23:00:00）
df3.index = df3.index + timedelta(hours = -1)
# 指定した範囲でdfを抽出（置換）
df3 = df3[(df3.index >= d_ld) & (df3.index <= d_td)]

print(df3)

# 60分データから日平均値を算出する
df_mean = df3.resample("1D").mean()

print(df_mean)

# 全データ （np_mean[日付index, データ項目column]の２次元配列）
np_mean = df_mean.values
np_max = df_max.values
np_min = df_min.values

print(np_mean)

# 前日のみ抽出 （インデックス-1は最後の意味）
np_mean_yd = np_mean[-1]
np_max_yd = np_max[-1]
np_min_yd = np_min[-1]

# 変数に入れる(col1を指定したい。0から始まるので、1列目のハウス内温度１は0,2列目の･･･は1のようになる）
#ハウスの温度 
house_temp_mean_1 = Decimal(np_mean[-1, 0]).quantize(Decimal('0.1'),rounding = ROUND_HALF_UP)
house_temp_max_1 = np_max[-1, 0]
house_temp_min_1 = np_min[-1, 0]

# 日付をindexから取得する
index = df_mean.index.date
index_str = df_mean.index.strftime('%Y-%m-%d')

# LINE notify のURL
url99 = "https://notify-api.line.me/api/notify"
token = '通知するLINEグループのアクセストークン'

# LINEグループに通知を行う(１枚目の画像を送る)
message = '\n'
message+= "■ハウス温度" + '\n'
message+= str(index[-1]) + '\n'
message+= '平均温度' + str(house_temp_mean_1) + " ℃" + '\n'
message+= '最高温度' + str(house_temp_max_1) + " ℃" + '\n'
message+= '最低温度' + str(house_temp_min_1) + " ℃"

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph1.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)

#"""
# LINEグループに通知を行う(２枚目の画像を送る)
message = '\n'
message+= "■ハウス湿度" + '\n'
message+= str(index[-1])

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph2.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)

# LINEグループに通知を行う(３枚目の画像を送る)
message = '\n'
message+= "■地温" + '\n'
message+= str(index[-1]) 

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph3.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)

# LINEグループに通知を行う(４枚目の画像を送る)
message = '\n'
message+= "■土壌水分" + '\n'
message+= str(index[-1]) 

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph4.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)

# LINEグループに通知を行う(５枚目の画像を送る)
message = '\n'
message+= "ハウス情報まとめ" + '\n'
message+= str(index[-1]) 

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph5.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)

# LINEグループに通知を行う(６枚目の画像を送る)
message = '\n'
message+= "ハウス温度と地温" + '\n'
message+= str(index[-1]) 

payload = {'message' : message}
headers = {'Authorization' : 'Bearer '+ token}
files = {"imageFile":open("graph6.png","rb")}
r = requests.post(url99, data=payload, headers=headers, files = files)
#"""

"""
本プログラムはβ版です。
Python3.7.3、Numpy1.20.1、Pandas1.2.2、Matplotlib3.3.4で動作確認しておりますが、
ご使用になられる環境での動作保証は致しておりません。
"""