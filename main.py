from translate import translate
import telebot # pyTelegramBotAPI


TOKEN = 'YOUR TOKEN'
tarjimon_bot = telebot.TeleBot(token=TOKEN)

# /start komandasi uchun mas'ul funksiya
@tarjimon_bot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum, tarjimon botiga xush kelibsiz!"
    xabar += '\nMatningizni yuboring.'
    tarjimon_bot.reply_to(message, xabar)
# botni ishga tushiramiz
# tarjimon_bot.polling()

# matnlar uchun mas'ul funksiya
@tarjimon_bot.message_handler(func=lambda  msg:  msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimon_bot.reply_to(message, translate(msg))

# botni ishga tushiramiz
tarjimon_bot.polling()