﻿# FinancialBot
Телеграм-бот для учёта расходов в Google Sheets
### Стэк
telebot, gspread
### Этапы работы:
- Подключение к Google Sheets с помощью библиотеки gspread и Google Sheets API
- Настройка клавиатур для взаимодействия с пользователем
- Создание функции для добавления кнопок в клавиатуру на основе предопределённых словарей (button_menu_info, button_category_info, button_month_info)
- Написание функций для обработки команд от пользователя (/start) и нажатий на кнопки (callback_query_handler). Функции вызываются с помощью декораторов, реагирующих на разные типы команд.
- Запись данных в Google Sheets с помощью метода append_row

### Реализованные функции:
- Выбор даты
- Выбор категории
- Внесение расходов
### Функции в разработке:
- Добавление и удаление категорий
- Просмотр статистики расходов 
- Авторизация пользователя
  
Дополнительно планирую сделать сводную, удобную для пользователя таблицу в Google Sheets, на основе данных из той, которой пользуется бот.
<div align="center"">
<img src="https://sun9-6.userapi.com/impg/M9XRC46wD7rEUN_5qmzkQsTxIaL4RljphUjHKQ/MGQyJFHOh6k.jpg?size=671x1280&quality=95&sign=986a417ac6c9616004a8bbec384adbe1&type=album" width="200" height="400">
  <img src="https://sun9-77.userapi.com/impg/iJ2fwmGFqUys4duJDGKxEzNoRi5-X6_ZlQBxRg/uMXTit7eCKE.jpg?size=676x1280&quality=95&sign=88abc10d377d0b81dfeab029e19ca895&type=album" width="200" height="400">
  <img src="https://sun9-52.userapi.com/impg/oSgv-I8WBIWA-HZECABzuGy2AhsbIkxq6iK8QA/9L3Ef-Q2oC0.jpg?size=670x1280&quality=95&sign=279a173dee08ff3c48671af5c2dfe76e&type=album" width="200" height="400">
   <img src="https://sun9-50.userapi.com/impg/tY6Ya3SdZdXYg72V-Dl_bpjBGHoP_3UWcdjiNA/zASdXEHT7Gc.jpg?size=795x719&quality=95&sign=dd413a0653acc8c75d9c3a144252b579&type=album" width="400" height="300">
</div>
