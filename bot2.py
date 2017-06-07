import sys
import time
import telepot

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        aux = msg['text']
        if 'woman' in aux:
           bot.sendMessage(chat_id, text='joder buy her a jewel! https://www.swarovsky.com/')
        elif 'man' in aux:
           bot.sendMessage(chat_id, text='buy him a pizza. if you are lazy call telepizza, I got a coupon for it')
        elif 'boy' in aux:
           bot.sendMessage(chat_id, text='pagale una puta')


TOKEN = sys.argv[0]  # get token from command-line

bot = telepot.Bot('305526886:AAGyi4p6pHVKeM9cMFarVMLPywK9UvP5evw')
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

