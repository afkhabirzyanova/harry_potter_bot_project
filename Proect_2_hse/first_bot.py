import telebot  # импортируем модуль pyTelegramBotAPI
import conf  # импортируем наш секретный токен
import requests
from telebot import types

# telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'} #задаем прокси
# telebot.apihelper.proxy = conf.PROXY #прокси из conf.py
bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота

# создаем клавиатуру
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте, " + message.from_user.first_name + "! Давайте проверим\
    как хорошо вы можете отличить оригрнал от сгенерированного теста. За основу берется перевод Гаррри Потрера\
    на русский язык от росмэн. За одну игру будет 10 заданий. За каждое верное задание вам начисляется 1 балл.\
    Ваши ответы будут сохранены. В самом конце нажав на кнопку 'Статистика' вы сможете посмотреть статистику как\
    хорошо пользователи угадывают в среднем. С вами параллельно будет играть бот. В конце вы можете начать игру\
    заново или посмотреть статистику. Чтобы выйти из игры нажмите 'Exit'")

    # добавляем на нее две кнопки
    button1 = types.KeyboardButton(text="Начать игру")
    button2 = types.KeyboardButton(text="Статистика")
    keyboard.add(button1, button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Что хотите сделать?", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Начать игру":
            button3 = types.KeyboardButton(text="Выйти")
            button6 = types.KeyboardButton(text="1")
            button7 = types.KeyboardButton(text="2")
            button2 = types.KeyboardButton(text="Статистика")
            keyboard.add(button3, button6, button7, button2)

            bot.send_message(message.chat.id, "b", reply_markup=keyboard)

        elif message.text == "Статистика":
            button1 = types.KeyboardButton(text="Начать игру")
            button3 = types.KeyboardButton(text="Выйти")
            button5 = types.KeyboardButton(text="Правило игры")
            keyboard.add(button1, button3, button5)

            bot.send_message(message.chat.id, "Статистика", reply_markup=keyboard)


# # функция запустится, когда пользователь нажмет на кнопку
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.message:
#         if call.data == "button1":
#             bot.send_message(call.message.chat.id, "Вы нажали на первую кнопку.")
#         if call.data == "button2":
#             bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")


# этот обработчик запускает функцию send_welcome,
# когда пользователь отправляет команды /start или /help
# @bot.callback_query_handler(func=lambda call: True)
# def bop(call):
#     contents = requests.get('https://random.dog/woof.json').json()
#     url = contents['url']
#     bot.send_photo(chat_id=message.chat.id, photo=url)
#
#
# #создаем словарь
# notes = {}

# @bot.message_handler(commands=['remind'])
# def remind(message):
#     user_id = message.chat.id
#     if user_id not in notes:
#         bot.send_message(user_id, "Вы мне еще не писали.")
#     else:
#         bot.send_message(user_id, notes[user_id])
#
# @bot.message_handler(content_types=['text'])
# def remember(message):
#     user_id = message.chat.id
#     notes[user_id] = message.text
#     bot.send_message(user_id, "Я запомнил")
#
#
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id,
#                      "Здравствуйте! Давайте проверим как хорошо вы можете отличить оригрнал от сгенерированного теста.\n"
#                      "За основу берется перевод Гаррри Потрера на русский язык от росмэн.\n"
#                      "За одну игру будет 10 заданий. За каждое верное задание вам начисляется 1 балл.\n"
#                      "Ваши ответы будут сохранены. В самом конце нажав на кнопку 'Статистика' вы сможете \n"
#                      "посмотреть статистику как хорошо пользователи угадывают в среднем. С вами параллельно будет\n"
#                      " играть бот. В конце вы можете начать игру заново или посмотреть статистику. Чтобы выйти из \n"
#                      "игры нажмите 'Exit'")
#
#
# # этот обработчик реагирует на любое сообщение
# @bot.message_handler(func=lambda m: True)
# def send_len(message):
#     bot.send_message(message.chat.id,
#                      'В вашем сообщении {} символов.'.format(len(message.text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
