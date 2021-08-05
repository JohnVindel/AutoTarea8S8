#Tarea 8 - Formula de Grados ºC y ºK
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['celcius-kelvin', 'c-k', 'kelvin'])
def info(mensaje):
    bot.reply_to(mensaje, "ºK= ºC + 273.15")
    print("Celcius a Kelvin")

@bot.message_handler(commands=['kelvin-celcius', 'k-c', 'celcius'])
def info(mensaje):
    bot.reply_to(mensaje, "ºC= ºK - 273.15")
    print("Fahrenheit a Celcius")

bot.polling()