import telebot
import parser
from telebot import types

#main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

#handlers
@bot.message_handler(commands=['start'])
def welcome(message):
	
	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Информация") 
	item2 = types.KeyboardButton("Стать волонтером!")
	item3 = types.KeyboardButton("Контакты")
	item4 = types.KeyboardButton("О нас")

	markup.add(item1, item2, item3, item4)

			
	bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)		

@bot.message_handler(content_types=['text'])
def lalala(message):
		if message.text == "Информация":
			bot.send_message(message.chat.id, 'Всю информацию в скором времени можно найти в нашем Instagram https://www.instagram.com/ast.green.tree/?hl=ru')
		elif message.text == 'Стать волонтером!':
			bot.send_message(message.chat.id, 'Перейдите в группу с волонтерами и ожидайте скорых ивентов) https://chat.whatsapp.com/LoMCvoBzJEhFInMBc23X96')
		elif message.text == 'Контакты':
			bot.send_message(message.chat.id, 'Контакты команды доступны в группе WhatsUp. По предложениям и вопросам сотрудничества: ast.green.tree@gmail.com')
		elif message.text == 'О нас':
			bot.send_message(message.chat.id, 'Мы волонтерская организация, созданная в цели улучшения экологии, и озеленении Казахстана.')
		else:
			bot.send_message(message.chat.id, "Не совсем понимаю, напишите одну из предложенных команд =)")



bot.polling(none_stop=True)
