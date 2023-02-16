import telebot

bot = telebot.TeleBot("6238405622:AAG73Ow0V_f02fsL2O3L6PrvCFxGQ1Gg6qk", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	print(message.text)
	bot.reply_to(message, message.text)

bot.infinity_polling()    