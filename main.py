#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1940171645:AAHJ0cLL2I14-4ihDr5E6y18x7wMJ9FpSq8'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
BOT dello shop di TechnoStyle
Per aprire questa guida fare /start o /help

Netflix   0,50 Euro    /netflix
Spotify   0,50 Euro    /spotify
Disney+   0,50 Euro    /disney+
Dazn      0,50 Euro    /dazn
Minecraft 0,50 Euro    /minecraft

I PREZZI SOPRA SONO DA PAGARE SOLO ALL'ACQUISTO, NON AL MESE/ANNO


Per informazioni contatta @fyreck
Per informazioni su come pagare scrivi /infopagamento\
ATTENZIONE ALLE MAIUSCOLE


Cosa vorresti comprare?\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text=='/infopagamento':
         bot.reply_to(message,'Effettua il pagamento su questo link https://paypal.me/fyreck, fai lo screen della ricevuta e mandalo a @fyreck che provvederà a validare il pagamento e a darti il tuo acquisto')

    elif message.text=='/netflix':
         bot.reply_to(message,'Effettua un pagamento di 0,50 Euro su https://paypal.me/fyreck')

    elif message.text=='/spotify':
         bot.reply_to(message,'Effettua un pagamento di 0,50 Euro su https://paypal.me/fyreck')

    elif message.text=='/disney+':
         bot.reply_to(message,'Effettua un pagamento di 0,50 Euro su https://paypal.me/fyreck')
      
    elif message.text=='/dazn':
         bot.reply_to(message,'Effettua un pagamento di 0,50 Euro su https://paypal.me/fyreck')
        
    elif message.text=='/minecraft':
         bot.reply_to(message,'Effettua un pagamento di 0,50 Euro su https://paypal.me/fyreck')

    else:
        bot.reply_to(message,'Controlla di aver scritto il comando correttamente.')


bot.polling()