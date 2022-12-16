import telebot
import sqlite3
from datetime import datetime

bot = telebot.TeleBot('5671932995:AAHKmaMS_8jxylQYSNaqLyy6qL4ZpKrfMT0')

conn = sqlite3.connect("database.db", check_same_thread = False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Неделя_1(
                    Понедельник TEXT,
                    Вторник TEXT,
                    Среда TEXT,
                    Четверг TEXT,
                    Пятница TEXT,
                    Суббота TEXT);
                """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Неделя_2(
                    Понедельник TEXT,
                    Вторник TEXT,
                    Среда TEXT,
                    Четверг TEXT,
                    Пятница TEXT,
                    Суббота TEXT);
                """)

week_1 = ['<ВвИТ(лекция)> <221(ОП)> <09:30-11:05> <Машковцева Л.С.>\n<ВвИТ(практика)> <328(ОП)> <11:20-12:55> <Рабенандрасана Жослен>\n<Высшая математика(лекция)> <514(ОП)> <13:10-14:45> <Александров Ю.Л.>\n<Высшая математика> <504(ОП)> <15:25-17:00> <Александров Ю.Л.>\n',
'<Физика(лекция)> <226(ОП)> <13:10-14:45> <Иноземцева Н.Г.>\n<История(лекция)> <301(ПО)> <15:25-17:00> <Скляр Л.Н.>\n<Физика(лекция)> <226(ОП)> <17:15-18:50> <Иноземцева Н.Г.>\n',
'<ВвИТ(лекция)> <344(ОП)> <9:30-11:05> <Машковцева Л.С.>\n<Физическая культура и спорт(практика)> <Спортзал №2(ОП)> <11:20-12:55> <Волохова С.В.>\n<История(практика)> <318(ОП)> <13:10-14:45> <Скляр Л.Н.>\n',
'Занятий в этот день нет\n',
'<ВвИТ(лаб. занятие)> <328(ОП)> <11:20-12:55> <Рабенандрасана Жослен>\n<Физическая культура и спорт(практика)> <Спортзал №2(ОП)> <13:10-14:45> <Волохова С.В.>\n',
'Занятий в этот день нет\n']

week_2 = ['<Иностранный язык(практика)> <410(ОП)> <09:30-11:05> <Павлова А.Ю.>\n<Высшая математика(практика)> <424(ОП)> <11:20-12:55> <Александров Ю.Л.>\n<Русский язык и культура речи(практика)> <314(ОП)> <13:10-14:45> <Горшкова Д.И.>\n',
'<ВвИТ(практика)> <324(ОП)> <11:20-12:55> <Рабенандрасана Жослен>\n<Физическая культура и спорт(практика)> <Спортзал №3(ОП)> <13:10-14:45> <Волохова С.В.>\n<Физика(практика)> <324(ОП)> <15:25-17:00> <Иноземцева Н.Г.>\n',
'<Введение в профессию(практика)> <Л-413(А)> <9:30-11:05> <Маликова Е.Е.>\n<Физическая культура и спорт(практика)> <Спортзал(А)> <11:20-12:55> <Волохова С.В.>\n',
'<Иностранный язык(практика)> <302(ОП)> <09:30-11:05> <Павлова А.Ю.>\n<Высшая математика(лекция)> <526(ОП)> <11:20-12:55> <Александров Ю.Л.>\n<Русский язык и культура речи(лекция)> <344(ОП)> <13:10-14:45> <Горшкова Д.И.>\n<История(практика)> <318(ОП)> <15:25-17:00> <Скляр Л.Н.>\n<Физика(лаб.занятие)> <342(ОП)> <17:15-18:50> <Сирко И.В.//Файзулаев В.Н.>\n',
'Занятий в этот день нет\n',
'Занятий в этот день нет\n']

cursor.execute("INSERT INTO Неделя_1 VALUES(?, ?, ?, ?, ?, ?);", week_1)
cursor.execute("INSERT INTO Неделя_2 VALUES(?, ?, ?, ?, ?, ?);", week_2)

days_list = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
week_number = datetime.today().isocalendar()[1] % 2


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Расписание на текущую неделю", "Расписание на следующую неделю")
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота")
    bot.send_message(message.chat.id, "Расписание на какой день вы хотите увидеть?", reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def week(message):
    if week_number == 1:
        bot.send_message(message.chat.id, "Сейчас идёт нечётная неделя")
    else:
        bot.send_message(message.chat.id, "Сейчас идёт чётная неделя")


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, "Сайт МТУСИ: https://mtuci.ru/")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Описание доступных команд:\n"
                                      "/help - помощь по доступным командам\n"
                                      "/week - четная/нечетная неделя\n"
                                      "/mtuci - ссылка на официальный сайт МТУСИ\n"
                                      "Нажмите на кнопку нужного дня или недели для вывода расписания")


@bot.message_handler(content_types='text')
def reply(message):
    if message.text.lower() in days_list:
        if week_number == 1:
            cursor.execute("SELECT * FROM Неделя_1")
        else:
            cursor.execute("SELECT * FROM Неделя_2")
        records = cursor.fetchone()
        text = f"{message.text}:\n"
        text += '____________________________________________________________\n'
        for row in range(6):
            if row == days_list.index(message.text.lower()):
                text += str(records[row]) + "\n"
            else: 
                continue
        text += "____________________________________________________________"
        bot.send_message(message.chat.id, text)
    elif 'текущую' in message.text.lower():
        text = ""
        if week_number == 1:
            cursor.execute("SELECT * FROM Неделя_1")
        else:
            cursor.execute("SELECT * FROM Неделя_2")
        records = cursor.fetchone()
        text += 'Текущая неделя\n'
        text += '____________________________________________________________\n'
        for i in records:
            text += str(i) + "\n"
        text += "____________________________________________________________"
        text += '\n\n'
        bot.send_message(message.chat.id, text)
    elif 'следующую' in message.text.lower():
        text = ""
        if week_number + 1 == 1:
            cursor.execute("SELECT * FROM Неделя_1")
        else:
            cursor.execute("SELECT * FROM Неделя_2")
        records = cursor.fetchone()
        text += 'Следующая неделя\n'
        text += '____________________________________________________________\n'
        for i in records:
            text += str(i) + "\n"
        text += "____________________________________________________________"
        text += '\n\n'
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Извините, я Вас не понял")



bot.infinity_polling()