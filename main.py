import telebot
from telebot import types

TOKEN = "7320930378:AAESFjBnBgi6wfHQvsuuNGMb-8_T6-LUE94"
bot = telebot.TeleBot(TOKEN)

#Creación d ecomandos simples como `/start` y `/help`

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hola! Soy tu primer bot creado con TeleBot")

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "Puedes interactuar conmigo usando los comandos `/start` y `/help`")

#@bot.message_handler(func=lambda m:True)
#def echo_all(message):
   # bot.reply_to(message, message.text)

@bot.message_handler(commands=["pizza"])
def send_opcions(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    #Creando botones
    btn_si=types.InlineKeyboardButton("Si", callback_data="pizza_si")
    btn_no=types.InlineKeyboardButton("No", callback_data="pizza_no")

    #Agrega botones al markup
    markup.add(btn_si, btn_no)

    #Enviar mensajes con los botones
    bot.send_message(message.chat.id, "Te gusta la Pizza?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback_uery(call):
    if call.data == "pizza_si":
        bot.answer_callback_query(call.id, "A mi también")
    elif call.data == "pizza_no":
        bot.answer_callback_query(call.id, "Bueno, cada cual tiene sus gustos")



@bot.message_handler(commands=["foto"])
def send_image(message):
    img_url="https://www.google.com/imgres?q=imagen%20de%20python&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fc%2Fc3%2FPython-logo-notext.svg%2F1869px-Python-logo-notext.svg.png&imgrefurl=https%3A%2F%2Fes.m.wikipedia.org%2Fwiki%2FArchivo%3APython-logo-notext.svg&docid=eL2wSjdlxA46nM&tbnid=CVQvyaOpjfIJxM&vet=12ahUKEwiboLyQ79OHAxWLqZUCHQkFCP4QM3oECGoQAA..i&w=1869&h=2048&hcb=2&ved=2ahUKEwiboLyQ79OHAxWLqZUCHQkFCP4QM3oECGoQAA"
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption="Aqui tienes tu imagen")




if __name__=="__main__":
    bot.polling(non_stop=True)


