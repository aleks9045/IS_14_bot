import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from keyboards import weeks_keyboard, top_week_keyboard, lower_week_keyboard, main_keyboard
from bd_user_id import check_user_id
from work_with_DB import BotDB_top, BotDB_lower
from DB_photos import PhotosDB_top
from deep_translator import GoogleTranslator

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5943456648:AAHnaCeOanZYMK4T8mKHlRIg267Bb2_C6PA")
dp = Dispatcher(bot)

BotDB_top = BotDB_top(r'Databases/top_week.db')
BotDB_lower = BotDB_lower(r'Databases/lower_week.db')
PhotosDB_top = PhotosDB_top(r'Databases/top_week_image.db')


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Вас приветствует бот, созданный, чтобы говорить вам ваше домашнее задание. "
                         "Введите /help , чтобы узнать функционал бота и открыть клавиатуру с командами.\n"
                         "Все предложения и замечания, касающиеся бота писать @aleks_9045 и @Shuv1_Wolf\n"
                         "Особые благодарности:Даниил Болгов, Михаил Скуратов, Алексей Веденёв.")


@dp.message_handler(commands=["help"])
async def help_me(message: types.Message):
    await message.answer("Команды:\n"
                         "/hometask - Раздел, где вы можете узнать домашнее задание.\n"
                         "/about_add - Раздел, где вы можете узнать, как добавить домашнее задание.\n"
                         "/remove_keyboard - Команда, которая прячет дополнительную клавиатуру.",
                         reply_markup=main_keyboard)


@dp.message_handler(commands=["my_id"])
async def my_id(message: types.Message):
    await message.answer(message.from_user.id)


@dp.message_handler(commands=["about_add"])
async def add_hometask(message: types.Message):
    await message.answer('С помощью команды /add вы можете добавлять задания, '
                         'после команды нужно написать тип недели, день недели, предмет, и само задание. '
                         'Пример использования:\n'
                         '/add нижняя понедельник математика Сделать номер 128 и 129\n'
                         '/add верхняя четверг иностранный_язык(<--внимание на нижнее подчеркивание) '
                         'выучить словарные слова на стр. 111\n'
                         'Также при добавлении домашки нельзя использовать запятые и скобки(скоро исправим)')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photos_upload(message: types.Message):
    if check_user_id(message.from_user.id):
        file_id = message.photo[-1].file_id
        await bot.send_message(chat_id=message.from_user.id, text='Скопируйте следующее сообщение '
                                                                  'и вставьте после /photo <день недели> <предмет>')
        await bot.send_message(chat_id=message.from_user.id, text=file_id)
    else:
        pass


@dp.message_handler(commands='photo')
async def photos_upload(message: types.Message):
    if check_user_id(message.from_user.id):
        try:
            stroka = message.text.split()
            week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[1])).lower()
            PhotosDB_top.add_photo(f'"{week_day_ru}"', f'"{stroka[2]}"', f'"{stroka[3]}"')
            await message.answer('Вы успешно загрузили фотографию.')
        except Exception as ex:
            print(ex)
    else:
        pass


@dp.message_handler(commands=["add"])
async def add_hometask(message: types.Message):
    if check_user_id(message.from_user.id):
        stroka = message.text.split()
        if stroka[1].lower() == 'верхняя':
            try:
                stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i > 3])
                stroka_with_subject = stroka[3].lower()
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                await BotDB_top.add_homework_top(f'"{week_day_ru}"', f'"{stroka_with_subject}"', f'"{stroka_with_task}"')
                await message.answer('Вы успешно добавили задание.')
            except Exception as ex:
                print(ex)
                await message.answer('Произошла ошибка.')
        elif stroka[1].lower() == 'нижняя':
            try:
                stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i > 3])
                stroka_with_subject = stroka[3].lower()
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                await BotDB_lower.add_homework_lower(f'"{week_day_ru}"', f'"{stroka_with_subject}"', f'"{stroka_with_task}"')
                await message.answer('Вы успешно добавили задание.')
            except Exception as ex:
                print(ex)
                await message.answer('Произошла ошибка.')
        else:
            await message.answer('Вы не выбрали тип недели.')
    else:
        await message.answer('Вы не можете добавлять задания.')


@dp.message_handler(commands=["remove_keyboard"])
async def remove_keyboard(message: types.Message):
    await message.answer("Клавиатура скрыта.", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["hometask"])
async def hometask(message: types.Message):
    await message.answer("Выберите неделю", reply_markup=weeks_keyboard)


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


@dp.callback_query_handler(lambda call: call.data == 'top_week_monday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, понедельник:\n\n\n{BotDB_top.monday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('monday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


@dp.callback_query_handler(lambda call: call.data == 'top_week_tuesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, вторник:\n\n\n{BotDB_top.tuesday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('tuesday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


@dp.callback_query_handler(lambda call: call.data == 'top_week_wednesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, среда:\n\n\n{BotDB_top.wednesday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('wednesday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


@dp.callback_query_handler(lambda call: call.data == 'top_week_thursday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, четверг:\n\n\n{BotDB_top.thursday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('thursday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


@dp.callback_query_handler(lambda call: call.data == 'top_week_friday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, пятница:\n\n\n{BotDB_top.friday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('friday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


@dp.callback_query_handler(lambda call: call.data == 'top_week_saturday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, суббота:\n\n\n{BotDB_top.saturday_top()}',
                           reply_markup=main_keyboard)
    for i in PhotosDB_top.check_photos('saturday'):
        if i != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=i)


# Тут короче разделение недель, чтоб код понятней был


@dp.callback_query_handler(lambda call: call.data == 'lower_week_monday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, понедельник:\n\n\n{BotDB_lower.monday_lower()}',
                           reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_tuesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, вторник:\n\n\n{BotDB_lower.tuesday_lower()}',
                           reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_wednesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, среда:\n\n\n{BotDB_lower.wednesday_lower()}',
                           reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_thursday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, четверг:\n\n\n{BotDB_lower.thursday_lower()}',
                           reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_friday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, пятница:\n\n\n{BotDB_lower.friday_lower()}',
                           reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_saturday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, суббота:\n\n\n{BotDB_lower.saturday_lower()}',
                           reply_markup=main_keyboard)


async def main():
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())
except Exception as ex:
    print(ex)
