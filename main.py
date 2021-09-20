import telebot
# from telebot import *
from telebot import types

bot = telebot.TeleBot('2023143366:AAGYVrMtP7gj82ckSkjB88_0j_GSN4JpjUc')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://teachmeskills.by/"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, просто кликай на кнопку и начинай прямо сейчас",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def open_insta(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить Инстаграмм страницу ",
                                          url="https://instagram.com/teachmeskills?utm_medium=copy_link"))
    bot.send_message(message.chat.id,
                     "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас: "
                     "<a href='https://instagram.com/teachmeskills?utm_medium=copy_link'>InstTeachMeSkills</a>",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Front End разработчик')
    btn2 = types.KeyboardButton('Python разработчик')
    btn3 = types.KeyboardButton('Java разработчик')
    btn4 = types.KeyboardButton('Automation QA Engineer')
    btn5 = types.KeyboardButton('Android разработчик')
    btn6 = types.KeyboardButton('iOS разработчик')
    btn7 = types.KeyboardButton('Project Manager')
    btn8 = types.KeyboardButton('Business Analyst')
    btn9 = types.KeyboardButton('Unity-разработчик')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    send_mess = f"<b>Привет {message.from_user.first_name} " \
                f"{message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать тест заново?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Front End разработчик')
        btn2 = types.KeyboardButton('Python разработчик')
        btn3 = types.KeyboardButton('Java разработчик')
        btn4 = types.KeyboardButton('Automation QA Engineer')
        btn5 = types.KeyboardButton('Android разработчик')
        btn6 = types.KeyboardButton('iOS разработчик')
        btn7 = types.KeyboardButton('Project Manager')
        btn8 = types.KeyboardButton('Business Analyst')
        btn9 = types.KeyboardButton('Unity-разработчик')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        final_message = "Решил попробовать что-то еще? /nВыбери какое направление тебя интересует:"


    elif get_message_bot == "automation qa engineer":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('На Python')
        btn2 = types.KeyboardButton('На Java')
        btn3 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Для автоматизированного тестирования надо выбрать направление. Выберите его:"

    elif get_message_bot == "на python":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по QA на Python",
                url="https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-python-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку"

    elif get_message_bot == "на java":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по QA на Java",
                       url="https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку"


    elif get_message_bot == "front end разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Front End",
                            url="https://teachmeskills.by/kursy-programmirovaniya/frontend-html-css-javascript-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "python разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Питону",
                                    url="https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "java разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Java",
                                        url="https://teachmeskills.by/kursy-programmirovaniya/obuchenie-java-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "android разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Android разработке",
                                    url="https://teachmeskills.by/kursy-programmirovaniya/android-razrabotka-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "ios разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по iOS разработке",
                                  url="https://teachmeskills.by/kursy-programmirovaniya/ios-swift-razrabotka-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "project manager":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы Project Manager в IT",
                                  url="https://teachmeskills.by/kursy-programmirovaniya/project-manager-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "business analyst":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по бизнес-анализу в IT",
                                  url="https://teachmeskills.by/kursy-programmirovaniya/business-analyst-minsk"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    elif get_message_bot == "unity-разработчик":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по разработке игр на Unity",
                                  url="https://teachmeskills.by/kursy-programmirovaniya/unity-game-developer"))
        final_message = "Для подробностей скорее кликай на ссылку и присоединяйся к нам"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Front End разработчик')
        btn2 = types.KeyboardButton('Python разработчик')
        btn3 = types.KeyboardButton('Java разработчик')
        btn4 = types.KeyboardButton('Automation QA Engineer')
        btn5 = types.KeyboardButton('Android разработчик')
        btn6 = types.KeyboardButton('iOS разработчик')
        btn7 = types.KeyboardButton('Project Manager')
        btn8 = types.KeyboardButton('Business Analyst')
        btn9 = types.KeyboardButton('Unity-разработчик')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        final_message = "Скорее кликай на кнопку ниже и выбирай!"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
