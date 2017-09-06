
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
 
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
 
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
 
    print 'Got command: %s' % command
 
    if command == 'on':
       bot.sendMessage(chat_id, on(2))
    elif command =='off':
       bot.sendMessage(chat_id, off(2))
 
bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print 'I am listening...'
 
while 1:
     time.sleep(10)
