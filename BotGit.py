import telebot
from telebot import types
import gspread
import googletrans
from googletrans import Translator
# import time
from gspread import Cell, Client, Spreadsheet, Worksheet


credentials = {}


gc = gspread.service_account_from_dict(credentials)

sh = gc.open_by_key('')

sh1 = sh.sheet1

token = ''

bot = telebot.TeleBot(token)

bot.temp_data = {}

button_menu_info = {
    'button_expenses': {'text': 'Внести расходы', 'callback_data': 'button_expenses'},
    'button_statistics': {'text': 'Посмотреть статистику', 'callback_data': 'button_statistics'}
}

button_names = {
    'button_food': '🥦 Продукты',
    'button_cafe': '🍹 Кафе', 'button_car': '🚙 Машина', 'button_taxi': '🚕 Такси', 'button_meds': '💊 Лекарства', 'button_health': '🏓 Красота и здоровье', 'button_home': '🧺 Дом', 'button_pedicure': '💅🏻 Педикюр', 'button_cat': '🐒 Ешка', 'button_clothes': '👗 Одежда', 'button_education': '📚 Образование'
}

button_category_info = {
    'button_food': {'text': '🥦 Продукты', 'callback_data': 'button_food'},
    'button_cafe': {'text': '🍹 Кафе', 'callback_data': 'button_cafe'},
    'button_clothes': {'text': '👗 Одежда', 'callback_data': 'button_clothes'},
    'button_car': {'text': '🚙 Машина', 'callback_data': 'button_car'},
    'button_taxi': {'text': '🚕 Такси', 'callback_data': 'button_taxi'},
    'button_meds': {'text': '💊 Лекарства', 'callback_data': 'button_meds'},
    'button_health': {'text': '🏓 Красота и здоровье', 'callback_data': 'button_health'},
    'button_home': {'text': '🧺 Дом', 'callback_data': 'button_home'},
    'button_education': {'text': '📚 Образование', 'callback_data': 'button_education'},
    'button_pedicure': {'text': '💅🏻 Педикюр', 'callback_data': 'button_pedicure'},
    'button_cat': {'text': '🐒 Ешка', 'callback_data': 'button_cat'}
}

button_month_info = {
    'button_july': {'text': 'Июль', 'callback_data': 'button_july'},
    'button_august': {'text': 'Август', 'callback_data': 'button_august'},
    'button_september': {'text': 'Сентябрь', 'callback_data': 'button_september'},
    'button_october': {'text': 'Октябрь', 'callback_data': 'button_october'},
    'button_november': {'text': 'Ноябрь', 'callback_data': 'button_november'},
    'button_december': {'text': 'Декабрь', 'callback_data': 'button_december'},

}

month_names = {'button_june': 'Июнь'}

markup_menu = types.InlineKeyboardMarkup(row_width=1)

markup_category = types.InlineKeyboardMarkup(row_width=3)

markup_month = types.InlineKeyboardMarkup(row_width=3)


def add_buttons_to_markup(markup, button_dict):
    for button_key in button_dict:
        button = types.InlineKeyboardButton(
            text=button_dict[button_key]['text'],
            callback_data=button_dict[button_key]['callback_data']
        )
        markup.add(button)


add_buttons_to_markup(markup_menu, button_menu_info)

add_buttons_to_markup(markup_category, button_category_info)

add_buttons_to_markup(markup_month, button_month_info)

markup_date = types.InlineKeyboardMarkup(row_width=5)
buttons = [types.InlineKeyboardButton(
    f'{i}', callback_data=f'{i}') for i in range(1, 32)]
markup_date.add(*buttons)


start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton("/start")
start_markup.add(start_button)


def add_category(button_dict, category_name, emoji=''):
    callback_data = f'button_{category_name}'
    button_dict[callback_data] = {
        'text': f'{emoji} {category_name.capitalize()}', 'callback_data': callback_data}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, "Привет ✌️", reply_markup=start_markup)
    bot.send_message(
        message.chat.id, "Выберите опцию из меню:", reply_markup=markup_menu)


@bot.callback_query_handler(func=lambda call: call.data in button_menu_info.keys())
def callback_options(call):
    if call.message:
        if call.data == 'button_statistics':
            bot.send_message(call.message.chat.id, 'Раздел в разработке')
        elif call.data == 'button_expenses':
            bot.send_message(call.message.chat.id,
                             'Выберите месяц', reply_markup=markup_month)


@bot.callback_query_handler(func=lambda call: call.data in button_month_info.keys())
def callback_month(call):
    if call.message:
        selected_month = call.data
        bot.temp_data['selected_month'] = selected_month
        bot.send_message(call.message.chat.id, 'Выберите дату',
                         reply_markup=markup_date)


@bot.callback_query_handler(func=lambda call: call.data.isdigit() and int(call.data) in range(1, 32))
def callback_date(call):
    if call.message:
        selected_date = call.data
        bot.temp_data['selected_date'] = selected_date
        bot.send_message(call.message.chat.id,
                         'Выберите категорию:', reply_markup=markup_category)


@ bot.callback_query_handler(func=lambda call: call.data in button_category_info.keys())
def callback_categories(call):
    if call.message:
        category = button_names[call.data]
        bot.temp_data['category'] = category
        bot.send_message(call.message.chat.id, 'Введите сумму')


@ bot.message_handler(content_types=['text'])
def process_amount_entry(message):
    try:
        amount = float(message.text)
        selected_date = bot.temp_data.get('selected_date')
        selected_month = bot.temp_data.get('selected_month')
        category = bot.temp_data.get('category')
        month = button_month_info[selected_month]['text']
        add_expense(selected_month, category, selected_date, amount)
        bot.send_message(
            message.chat.id, f'Категория: {category}\nВнесено: {int(amount)}руб\nМесяц: {month}\nДень: {selected_date}\n\nДля внесения суммы в эту же категорию, введите число.\n\nЧтобы выбрать другой день, вернитесь в главное меню', reply_markup=markup_category)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число.')


def add_expense(selected_month, category, selected_date, amount):
    sheet = sh.worksheet(button_month_info[selected_month]['text'])
    sheet.append_row([category, selected_date, amount])


print('Сработало')

bot.infinity_polling()
