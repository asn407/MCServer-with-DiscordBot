ForgeServerのログ監視＋通知システム
===
# はじめに
CurseForgeが提供するサーバー（以下ForgeServerと記す）の機能は主にサーバーの起動、操作、そして停止であり、プレイヤーのゲーム入退室を通知する機能は備わっていない。

したがって、watchdogで常にログファイルを監視し、必要に応じてDiscordのサーバーに通知を行うDiscord Botを作成した。
# 概要
更新されたログから以下の情報を検知した場合、Discordのサーバーに通知を行う。
1. プレイヤーがゲームに参加した
2. プレイヤーがゲームを退出した
3. プレイヤーが進捗を達成した

Discordサーバーには、以下の情報を通知する。
1. ゲームに参加した日時とプレイヤー名
2. ゲームに参加した日時とプレイヤー名
3.  進捗を達成した日時と進捗名とプレイヤー名

# 導入方法
## 必要なパッケージをインストール＆仮想環境構築
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
用意するもの
1. チャンネルのID
2. Botのトークン
3. マインクラフトのサーバーが生成する`latest.log`が保管されている絶対パス

それぞれを、`bot.py`の必要な箇所に入力する。
# 起動方法
```
(venv_4_Bot) $ python3 bot.py
```
# ソースコードの解説
この場では、ソースコードの解説は行わない。  
なお、技術書典16で販売予定である「TECHNOLOGICS VOL.4」では解説が掲載されているので、必要であればそちらを参照されたい。

URL：（2024年6月上旬より販売開始予定）
# Lisence

This project is licensed under the MIT License, see the LICENSE for details.
