import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from keyboards import weeks_keyboard, weeks_keyboard_add, top_week_keyboard, top_week_keyboard_add, \
    lower_week_keyboard, lower_week_keyboard_add, main_keyboard

from States import WriteHomeworkTop, WriteHomeworkLower, storage
from aiogram.dispatcher import FSMContext

from bd_user_id import check_user_id
from Databases_py.work_with_DB import BotDB_top, BotDB_lower
from Databases_py.DB_photos import PhotosDB_top, PhotosDB_lower

from Data.config import TOKEN


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


lst_of_days = ['top_monday', 'top_tuesday', 'top_wednesday', 'top_thursday', 'top_friday', 'top_saturday',
               'lower_monday', 'lower_tuesday', 'lower_wednesday', 'lower_thursday', 'lower_friday',
               'lower_saturday']

lst_of_days_add = ['top_monday_add', 'top_tuesday_add', 'top_wednesday_add', 'top_thursday_add',
                   'top_friday_add', 'top_saturday_add', 'lower_monday_add', 'lower_tuesday_add',
                   'lower_wednesday_add', 'lower_thursday_add', 'lower_friday_add', 'lower_saturday_add']

time_zone = []

BotDB_top = BotDB_top(r'Databases/top_week.db')
BotDB_lower = BotDB_lower(r'Databases/lower_week.db')
PhotosDB_top = PhotosDB_top(r'Databases/top_week_image.db')
PhotosDB_lower = PhotosDB_lower(r'Databases/lower_week_image.db')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """СТАРТ"""
    await message.answer("Вас приветствует бот, созданный, чтобы говорить вам ваше домашнее задание. "
                         "Введите /help , чтобы узнать функционал бота и открыть клавиатуру с командами.\n"
                         "Все предложения и замечания, касающиеся бота писать @aleks_9045 и @Shuv1_Wolf")


@dp.message_handler(commands=["help"])
async def help_me(message: types.Message):
    """ОБЩАЯ ИНФА"""
    await message.answer("Команды:\n"
                         "/hometask - Раздел, где вы можете узнать домашнее задание.\n"
                         "/about_add - Раздел, где вы можете узнать, как добавить домашнее задание.\n"
                         "/remove_keyboard - Команда, которая прячет дополнительную клавиатуру.\n",
                         reply_markup=main_keyboard)


@dp.message_handler(commands=["my_id"])
async def my_id(message: types.Message):
    """УЗНАТЬ СВОЙ ID"""
    await message.answer(message.from_user.id)


@dp.message_handler(commands=["about_add"])
async def about_add(message: types.Message):
    """ПРО ДОБАВЛЕНИЕ ДЗ"""
    await message.answer('С помощью команды /add вы можете добавлять задания.')


@dp.message_handler(commands=["add"])
async def add_hometask(message: types.Message):
    """ДОБАВЛЕНИЕ ДЗ"""
    if check_user_id(message.from_user.id):
        await message.answer("Выберите неделю для добавления дз:", reply_markup=weeks_keyboard_add)


@dp.callback_query_handler(lambda call: call.data == 'top_week_add' or call.data == 'top_week_add')
async def all_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    if callback.data == 'top_week_add':
        await bot.send_message(callback.from_user.id, 'Выберите день недели(верхняя):',
                               reply_markup=top_week_keyboard_add)
    elif callback.data == 'lower_week_add':
        await bot.send_message(callback.from_user.id, 'Выберите день недели(нижняя):',
                               reply_markup=lower_week_keyboard_add)
    else:
        await bot.send_message(callback.from_user.id, 'Произошла ошибка.')


@dp.callback_query_handler(lambda call: call.data in lst_of_days_add)
async def all_top(callback: types.CallbackQuery):
    distribution = callback.data.split('_')
    time_zone.append(distribution)
    if distribution[0] == 'top':
        try:
            await WriteHomeworkTop.add_text.set()
            await bot.answer_callback_query(callback.id)
            await bot.send_message(callback.from_user.id, 'Напишите предмет и задание через пробел.')
        except Exception as ex_:
            print(ex_)
    elif distribution[0] == 'lower':
        try:
            await WriteHomeworkLower.add_text.set()
            await bot.answer_callback_query(callback.id)
            await bot.send_message(callback.from_user.id, 'Напишите предмет и задание через пробел.')
        except Exception as ex_:
            print(ex_)


@dp.message_handler(state=WriteHomeworkTop.add_text)
async def remove_keyboard(message: types.Message):
    try:
        stroka = message.text.split()
        time_zone.append(stroka[0].lower())
        stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i >= 1])
        BotDB_top.add_homework_top(f'"{time_zone[0][1]}"', f'"{stroka[0].lower()}"', f'"{stroka_with_task}"')
        await WriteHomeworkTop.next()
        await message.answer("Вы успешно добавили домашнее задание")
        await message.answer("Теперь прикрепите фотографию или напишите /empty")
    except Exception as ex_:
        print(ex_)
        await message.answer('Произошла ошибка.')


@dp.message_handler(state=WriteHomeworkLower.add_text)
async def remove_keyboard(message: types.Message):
    try:
        stroka = message.text.split()
        time_zone.append(stroka[0].lower())
        stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i >= 1])
        BotDB_lower.add_homework_lower(f'"{time_zone[0][1]}"', f'"{stroka[0].lower()}"', f'"{stroka_with_task}"')
        await WriteHomeworkLower.next()
        await message.answer("Вы успешно добавили домашнее задание")
        await message.answer("Теперь прикрепите фотографию или напишите /empty")
    except Exception as ex_:
        print(ex_)
        await message.answer('Произошла ошибка.')


@dp.message_handler(state=WriteHomeworkTop.add_photo, commands=['empty'])
async def remove_keyboard(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Успешно!')


@dp.message_handler(state=WriteHomeworkTop.add_photo, content_types=types.ContentType.PHOTO)
async def remove_keyboard(message: types.Message, state: FSMContext):
    try:
        photo = message.photo[0].file_id
        print(time_zone)
        PhotosDB_top.add_photo(f'"{time_zone[0][1]}"', f'"{time_zone[1]}"', f'"{photo}"')
        time_zone.clear()
        await message.answer("Вы успешно добавили фотографию")
        await state.finish()
    except Exception as ex_:
        print(ex_)
        await message.answer('Произошла ошибка.')


@dp.message_handler(state=WriteHomeworkLower.add_photo, content_types=types.ContentType.PHOTO)
async def remove_keyboard(message: types.Message, state: FSMContext):
    try:
        photo = message.photo[0].file_id
        PhotosDB_lower.add_photo(f'"{time_zone[0][1]}"', f'"{time_zone[1]}"', f'"{photo}"')
        time_zone.clear()
        await message.answer("Вы успешно добавили фотографию")
        await state.finish()
    except Exception as ex_:
        print(ex_)
        await message.answer('Произошла ошибка.')


@dp.message_handler(commands=["remove_keyboard"])
async def remove_keyboard(message: types.Message):
    """УДАЛЕНИЕ КЛАВИАТУРЫ"""
    await message.answer("Клавиатура скрыта.", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["hometask"])
async def hometask(message: types.Message):
    await message.answer("Выберите тип недели", reply_markup=weeks_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'all_top_week' or call.data == 'all_lower_week')
async def all_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    if callback.data == 'all_top_week':
        await bot.send_message(callback.from_user.id, BotDB_top.get_full_homework_top().replace('*', ','))
    elif callback.data == 'all_lower_week':
        await bot.send_message(callback.from_user.id, BotDB_lower.get_full_homework_lower().replace('*', ','))


@dp.callback_query_handler(text='top_week')
async def top_week_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день недели (верхняя):',
                           reply_markup=top_week_keyboard)


@dp.callback_query_handler(text='lower_week')
async def lower_week_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день недели (нижняя):',
                           reply_markup=lower_week_keyboard)


@dp.callback_query_handler(lambda call: call.data in lst_of_days)
async def dz(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    distribution = callback.data.split('_')
    if distribution[0] == 'top':
        try:
            await bot.send_message(callback.from_user.id,
                                   f'Верхняя неделя, понедельник:\n\n\n' 
                                   f'{BotDB_top.get_homework_top(f"{distribution[1]}")}'.replace('*', ','),
                                   reply_markup=main_keyboard)

            for photo in PhotosDB_top.check_photos(f'{distribution[1]}'):
                if photo != '':
                    await bot.send_photo(chat_id=callback.from_user.id, photo=photo)
        except Exception as ex_:
            print(ex_)
    elif distribution[0] == 'lower':
        try:
            await bot.send_message(callback.from_user.id,
                                   f'Верхняя неделя, понедельник:\n\n\n' 
                                   f'{BotDB_lower.get_homework_lower(f"{distribution[1]}")}'.replace('*', ','),
                                   reply_markup=main_keyboard)

            for photo in PhotosDB_lower.check_photos(f'{distribution[1]}'):
                if photo != '':
                    await bot.send_photo(chat_id=callback.from_user.id, photo=photo)
        except Exception as ex_:
            print(ex_)


async def main():
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())
except Exception as ex:
    print(ex)
