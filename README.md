# 通い農業支援システム

　本ページは農研機構東北農業研究センターが、農林水産省委託事業「原発事故からの復興のための放射性物質対策に関する実証研究委託事業」によって開発したハウス遠隔監視システム「通い農業支援システム」の配布プログラム公開ページです。

![image1](image1.jpg)

　本システムはモジュール化された簡便なIoT機器を利用して、離れたハウスの温度等をスマホで遠隔監視できるようにするハウス遠隔監視システムです。

　ハウスごとに通信機能付きマイコンと温度センサを設置して遠隔監視システムを構築するには、IoTに関する知識やWEBサーバの構築またはクラウドサービスの契約が必要であり、容易には作成できません。そこで、データ取得用・メッセージ通知用のWeb APIを利用することで、一定の知識があれば利用できる、ハウス温度等の遠隔監視を簡便に実現するシステムを提案しています。

　本システムでは「温度等のデータを定期通知」、「しきい値を超えた際の警報通知」、「日平均値・最大値・最小値の通知」、「グラフでの通知」といった機能を持つハウス遠隔監視システムを作成できます。
 
 # 導入方法について

　導入方法についてのマニュアルは農研機構のホームページで公開予定です。公開されましたらこちらのページにURLのリンクを公開します。マニュアルを参照しながら利用する「クイックスタートガイド」についてはこちらのページで公開予定です。

 # 資材の入手先について
 
 　マニュアルにも記載しておりますが、マニュアルの公開に合わせて、最新の資材の入手先例を公開します。
 
 # 使用上の注意

　本プログラムはプロトタイプ（β版）です。Python3.7.3、Numpy1.20.1、Pandas1.2.2、Matplotlib3.3.4で動作確認しておりますが、ご使用になられる環境での動作保証はいたしておりません。

　本プログラムを使用したことにより発生したいかなる損害に対して、農研機構は責任を負いません。また、本プログラムを用いて作成した「通い農業支援システム」は、自己の責任において製作・利用する遠隔監視するシステムです。本システムを用いて生じた故障又は損害等に関しては一切の責任を負いかねますのでご了承ください。

　また、本プログラムの商業的な利用又は配布に関しては連絡してください。

　通い農業支援システムに関するご質問、支援要請等については
　http://www.naro.affrc.go.jp/laboratory/tarc/inquiry/index.html
 までお願いします。
