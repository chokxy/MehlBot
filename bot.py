import telebot
import datetime
import csv
import math

url = "https://api.telegram.org/bot792883545:AAE8RCcDhYtdFqr0mrUO44cefOH26DgKWbE/"
bot = telebot.TeleBot("792883545:AAE8RCcDhYtdFqr0mrUO44cefOH26DgKWbE")
day = datetime.datetime.now().day
weekday = datetime.datetime.today().weekday()
results = []

if weekday == 6:
    weekday = 5


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to m(EH)lbot!! \n For today's breakfast " +
                 "menu, enter /breakfast \n For today's dinner menu, enter /dinner")


@bot.message_handler(commands=['breakfast'])
def send_welcome(message):
    res = ""
    with open('EHMenu.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            results.append(row)
        for i in range(0, 5):
            item = results[int(math.ceil(day/7)*21+i)][weekday]
            res += item + "\n"
        bot.reply_to(message, "For today's breakfast we have: " + "\n" + res)


@bot.message_handler(commands=['dinner'])
def send_welcome(message):
    res = ""
    with open('EHMenu.csv', 'r') as csvfile1:
        reader = csv.reader(csvfile1, delimiter=',')
        for row in reader:
            results.append(row)
        for i in range(7, 28):
            item = results[int(math.ceil(day/7)*21+i)][weekday]
            res += item + "\n"
    bot.reply_to(message, "For today's dinner we have: " + "\n" + res)


bot.polling()
