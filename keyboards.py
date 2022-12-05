from aiogram.types import ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, KeyboardButton

weeks_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
weeks_keyboard_add = InlineKeyboardMarkup(resize_keyboard=True)

top_week_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
lower_week_keyboard = InlineKeyboardMarkup(resize_keyboard=True)

top_week_keyboard_add = InlineKeyboardMarkup(resize_keyboard=True)
lower_week_keyboard_add = InlineKeyboardMarkup(resize_keyboard=True)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_remove = ReplyKeyboardMarkup(resize_keyboard=True)
add_hometask_info = ReplyKeyboardMarkup(resize_keyboard=True)
photos_info = ReplyKeyboardMarkup(resize_keyboard=True)

main_hometask = KeyboardButton('/hometask')
keyboard_remove_command = KeyboardButton('/remove_keyboard')
add_hometask_info_command = KeyboardButton('/about_add')
photos_info_command = KeyboardButton('/about_photos')

top_week_command = InlineKeyboardButton('Верхняя неделя', callback_data='top_week')
lower_week_command = InlineKeyboardButton('Нижняя неделя', callback_data='lower_week')

top_week_command_add = InlineKeyboardButton('|Верхняя неделя|', callback_data='top_week_add')
lower_week_command_add = InlineKeyboardButton('|Нижняя неделя|', callback_data='lower_week_add')

all_top_week_command = InlineKeyboardButton('Вся верхняя неделя', callback_data='all_top_week')
all_lower_week_command = InlineKeyboardButton('Вся нижняя неделя', callback_data='all_lower_week')


dz_top_week_monday = InlineKeyboardButton('Понедельник', callback_data='top_monday')
dz_top_week_tuesday = InlineKeyboardButton('Вторник', callback_data='top_tuesday')
dz_top_week_wednesday = InlineKeyboardButton('Среда', callback_data='top_wednesday')
dz_top_week_thursday = InlineKeyboardButton('Четверг', callback_data='top_thursday')
dz_top_week_friday = InlineKeyboardButton('Пятница', callback_data='top_friday')
dz_top_week_saturday = InlineKeyboardButton('Суббота', callback_data='top_saturday')

dz_lower_week_monday = InlineKeyboardButton('Понедельник', callback_data='lower_monday')
dz_lower_week_tuesday = InlineKeyboardButton('Вторник', callback_data='lower_tuesday')
dz_lower_week_wednesday = InlineKeyboardButton('Среда', callback_data='lower_wednesday')
dz_lower_week_thursday = InlineKeyboardButton('Четверг', callback_data='lower_thursday')
dz_lower_week_friday = InlineKeyboardButton('Пятница', callback_data='lower_friday')
dz_lower_week_saturday = InlineKeyboardButton('Суббота', callback_data='lower_saturday')


dz_top_week_monday_add = InlineKeyboardButton('|Понедельник|', callback_data='top_monday_add')
dz_top_week_tuesday_add = InlineKeyboardButton('|Вторник|', callback_data='top_tuesday_add')
dz_top_week_wednesday_add = InlineKeyboardButton('|Среда|', callback_data='top_wednesday_add')
dz_top_week_thursday_add = InlineKeyboardButton('|Четверг|', callback_data='top_thursday_add')
dz_top_week_friday_add = InlineKeyboardButton('|Пятница|', callback_data='top_friday_add')
dz_top_week_saturday_add = InlineKeyboardButton('|Суббота|', callback_data='top_saturday_add')

dz_lower_week_monday_add = InlineKeyboardButton('|Понедельник|', callback_data='lower_monday_add')
dz_lower_week_tuesday_add = InlineKeyboardButton('|Вторник|', callback_data='lower_tuesday_add')
dz_lower_week_wednesday_add = InlineKeyboardButton('|Среда|', callback_data='lower_wednesday_add')
dz_lower_week_thursday_add = InlineKeyboardButton('|Четверг|', callback_data='lower_thursday_add')
dz_lower_week_friday_add = InlineKeyboardButton('|Пятница|', callback_data='lower_friday_add')
dz_lower_week_saturday_add = InlineKeyboardButton('|Суббота|', callback_data='lower_saturday_add')


top_week_keyboard.add(dz_top_week_monday, dz_top_week_tuesday, dz_top_week_wednesday, dz_top_week_thursday,
                      dz_top_week_friday, dz_top_week_saturday)

lower_week_keyboard.add(dz_lower_week_monday, dz_lower_week_tuesday, dz_lower_week_wednesday, dz_lower_week_thursday,
                        dz_lower_week_friday, dz_lower_week_saturday)


top_week_keyboard_add.add(dz_top_week_monday_add, dz_top_week_tuesday_add, dz_top_week_wednesday_add,
                          dz_top_week_thursday_add, dz_top_week_friday_add, dz_top_week_saturday_add)

lower_week_keyboard_add.add(dz_lower_week_monday_add, dz_lower_week_tuesday_add, dz_lower_week_wednesday_add,
                            dz_lower_week_thursday_add, dz_lower_week_friday_add, dz_lower_week_saturday_add)


weeks_keyboard.add(lower_week_command, top_week_command, all_lower_week_command, all_top_week_command)

weeks_keyboard_add.add(top_week_command_add, lower_week_command_add)

main_keyboard.add(main_hometask, add_hometask_info_command, photos_info_command, keyboard_remove_command)
