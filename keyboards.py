from aiogram.types import ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, KeyboardButton

weeks_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
top_week_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
lower_week_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_remove = ReplyKeyboardMarkup(resize_keyboard=True)

main_hometask = KeyboardButton('/hometask')
main_keyboard_remove = KeyboardButton('/remove_keyboard')

top_week_command = InlineKeyboardButton('Верхняя неделя', callback_data='top_week')
lower_week_command = InlineKeyboardButton('Нижняя неделя', callback_data='lower_week')

dz_top_week_monday = InlineKeyboardButton('Понедельник', callback_data='top_week_monday')
dz_top_week_tuesday = InlineKeyboardButton('Вторник', callback_data='top_week_tuesday')
dz_top_week_wednesday = InlineKeyboardButton('Среда', callback_data='top_week_wednesday')
dz_top_week_thursday = InlineKeyboardButton('Четверг', callback_data='top_week_thursday')
dz_top_week_friday = InlineKeyboardButton('Пятница', callback_data='top_week_friday')
dz_top_week_saturday = InlineKeyboardButton('Суббота', callback_data='top_week_saturday')

dz_lower_week_monday = InlineKeyboardButton('Понедельник', callback_data='lower_week_monday')
dz_lower_week_tuesday = InlineKeyboardButton('Вторник', callback_data='lower_week_tuesday')
dz_lower_week_wednesday = InlineKeyboardButton('Среда', callback_data='lower_week_wednesday')
dz_lower_week_thursday = InlineKeyboardButton('Четверг', callback_data='lower_week_thursday')
dz_lower_week_friday = InlineKeyboardButton('Пятница', callback_data='lower_week_friday')
dz_lower_week_saturday = InlineKeyboardButton('Суббота', callback_data='lower_week_saturday')


top_week_keyboard.add(dz_top_week_monday, dz_top_week_tuesday, dz_top_week_wednesday, dz_top_week_thursday,
                      dz_top_week_friday, dz_top_week_saturday)

lower_week_keyboard.add(dz_lower_week_monday, dz_lower_week_tuesday, dz_lower_week_wednesday, dz_lower_week_thursday,
                        dz_lower_week_friday, dz_lower_week_saturday)
weeks_keyboard.add(lower_week_command, top_week_command)

main_keyboard.add(main_hometask, main_keyboard_remove)