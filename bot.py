import re
import time
import datetime
import discord
from discord.ext import tasks, commands
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler

CHANNEL_ID = 1234567890123 # CHANGE YOUR CHANNEL ID
TOKEN = 'TOKEN IS HERE'
WATCH_DIR = '/home/user/logs.txt'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

class Message:
    def __init__(self, pattern, format_, color):
        self.pattern = pattern
        self.format_ = format_
        self.color = color
        self.text = ''

    def _time_(self):
        dt_time = datetime.datetime.now()
        dt_time = dt_time.strftime('[ %Y/%m/%d ] [ %H:%M:%S ]')
        return str(dt_time)

class MinecraftLogMonitor:
    def __init__(self):
        self.position = 0
        self.message_list = []
        self.message_list.append(Message(': (.*) joined the game', '\n{0}', 0x00ff00))
        self.message_list.append(Message(': (.*) left the game', '\n{0}', 0xff0000))
        self.message_list.append(Message(': (.*) has made the advancement (.*)', '\n{0} : {1}', 0x00aeef))

    def _get_(self):
        with open(WATCH_DIR, 'r', errors='ignore') as f:
            f.seek(self.position)
            logs = f.readlines()
            self.position = f.tell()

        for log in logs:
            for message in self.message_list:
                if match := re.search(message.pattern, log):
                    message.text = message.format_.format(*match.groups())
                    return message

        return None

    async def _send_(self, message):
        if message == None:
            return
        
        channel = bot.get_channel(CHANNEL_ID)
        final_text = message._time_() + message.text
        embed = discord.Embed(title=final_text, color=message.color)

        await channel.send(embed=embed)

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, monitor):
        self.monitor = monitor

    def on_modified(self, event):
        bot.loop.create_task(self.monitor._send_(self.monitor._get_()))

if __name__ == '__main__':
    @bot.event
    async def on_ready():
        monitor = MinecraftLogMonitor()
        observer = PollingObserver()
        observer.schedule(FileChangeHandler(monitor), path=WATCH_DIR, recursive=True)
        observer.start()

    bot.run(TOKEN)
