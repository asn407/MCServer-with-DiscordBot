マイクラ鯖のログ通知をDiscord Botに行わせる
===
# はじめに
マインクラフトのサーバーが提供する機能は主にサーバーの起動、操作、そして停止であり、ログをどこかに送信する機能はない。

従って、watchdogで常にログファイルを監視し、必要に応じてDiscordのサーバーに通知を行うDiscord Botを作成した。
# 概要
ログから以下の情報を検知した場合、Discordのサーバーに通知を行う。
1. ゲームに参加したプレイヤーとその時刻
2. ゲームから退場したプレイヤーとその時刻
3. 進捗達成したプレイヤーとその内容と達成時刻

# 導入方法
## 必要なパッケージをインストール＆環境構築
```
$ sudo apt update && sudo apt upgrade -y
```
```
$ sudo apt install python3.10-venv
```
```
$ python3 -m venv venv_4_Bot
```
```
$ source ./venv_4_Bot/bin/activate
```
```
(venv_4_Bot) $ python3 -m pip install discord.py
```
```
(venv_4_Bot) $ python3 -m pip install watchdog
```
## bot.pyの編集
用意する者
1. チャンネルのID
2. Botのトークン
3. マインクラフトのサーバーが生成する`latest.log`が保管されている絶対パス

それぞれを、`bot.py`の必要な箇所に入力する。
# 起動方法
```
(venv_4_Bot) $ python3 bot.py
```
