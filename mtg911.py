#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import telebot
from telebot.types import Message
import shutil

BASE_URL = 'https://api.telegram.org/bot735263028:AAFvj0eR3w-bp13YNue_pnswn22HADoEN18/'

r = requests.get(f'{BASE_URL}getMe')

r = requests.get(f'{BASE_URL}getUpdates')


import pprint
pprint.pprint(r.json())
print(len(r.json()['result']))



payload = {}
payload['chat_id'] = 159195360
payload['text'] = 'This and that'

print(payload)

r = requests.post(f'{BASE_URL}sendMessage',data=payload)

TOKEN = '735263028:AAFvj0eR3w-bp13YNue_pnswn22HADoEN18'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def upper(message:Message):
    bot.reply_to(message, message.text.upper())

bot.polling()

SEARCHCARD = 'Fanat Fire'.replace(' ','+')
SEARCHCARD = input('what card? ').replace(' ','+')
search_upd = f'https://api.scryfall.com/cards/named?fuzzy={SEARCHCARD}'
r = requests.get(search_upd)
api_respond = r.json()


print(api_respond)

print(api_respond['image_uris'])

request_image = api_respond['image_uris']['normal']
print(request_image)
r = requests.get(request_image, stream = True)
if r.status_code == 200:
    with open('test.jpg', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
else:
    print('smth went wrong')