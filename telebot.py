import time
import random
import datetime
import telepot
from subprocess import call
import subprocess
import os
from telepot.loop import MessageLoop
 
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print 'Got command: %s' % command
    if command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/speed':
        x = subprocess.check_output(['speedtest-cli','--share'])
        bot.sendMessage(chat_id,x)
    elif command == '/ip':
        x = subprocess.check_output(['curl','ipinfo.io/ip'])
        bot.sendMessage(chat_id,x)
    elif command == '/disk':
        x = subprocess.check_output(['df'])
        bot.sendMessage(chat_id,x)
    elif command == '/mem':
        x = subprocess.check_output(['cat','/proc/meminfo'])
        bot.sendMessage(chat_id,x)
    elif command == '/stat':
        bot.sendMessage(chat_id,'Number five is alive!')
    elif command == '/logo':
        bot.sendPhoto(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
    
 
bot = telepot.Bot('*** insert your bot token here')
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'
 
while 1:
    time.sleep(10)
