import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from keyboards import weeks_keyboard, top_week_keyboard, lower_week_keyboard, main_keyboard
from bd_user_id import check_user_id
from work_with_DB import BotDB_top, BotDB_lower
from DB_photos import PhotosDB_top, PhotosDB_lower
from deep_translator import GoogleTranslator

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5943456648:AAHnaCeOanZYMK4T8mKHlRIg267Bb2_C6PA")
dp = Dispatcher(bot)

BotDB_top = BotDB_top(r'Databases/top_week.db')
BotDB_lower = BotDB_lower(r'Databases/lower_week.db')
PhotosDB_top = PhotosDB_top(r'Databases/top_week_image.db')
PhotosDB_lower = PhotosDB_lower(r'Databases/lower_week_image.db')


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """СТАРТ"""
    await message.answer("Вас приветствует бот, созданный, чтобы говорить вам ваше домашнее задание. "
                         "Введите /help , чтобы узнать функционал бота и открыть клавиатуру с командами.\n"
                         "Все предложения и замечания, касающиеся бота писать @aleks_9045 и @Shuv1_Wolf\n"
                         "Особые благодарности:Даниил Болгов, Михаил Скуратов, Алексей Веденёв.")


@dp.message_handler(commands=["help"])
async def help_me(message: types.Message):
    """ОБЩАЯ ИНФА"""
    await message.answer("Команды:\n"
                         "/hometask - Раздел, где вы можете узнать домашнее задание.\n"
                         "/about_add - Раздел, где вы можете узнать, как добавить домашнее задание.\n"
                         "/remove_keyboard - Команда, которая прячет дополнительную клавиатуру.\n"
                         "/about_photos - Раздел, где вы можете узнать, как добавлять фотографии.",
                         reply_markup=main_keyboard)


@dp.message_handler(commands=["my_id"])
async def my_id(message: types.Message):
    """УЗНАТЬ СВОЙ ID"""
    await message.answer(message.from_user.id)


@dp.message_handler(commands=["about_add"])
async def about_add(message: types.Message):
    """ПРО ДОБАВЛЕНИЕ ДЗ"""
    await message.answer('С помощью команды /add вы можете добавлять задания, '
                         'после команды нужно написать тип недели, день недели, предмет, и само задание. '
                         'Пример использования:\n'
                         '/add нижняя понедельник математика Сделать номер 128 и 129\n'
                         '/add верхняя четверг иностранный_язык(<--внимание на нижнее подчеркивание) '
                         'выучить словарные слова на стр. 111\n'
                         'Также при добавлении домашки нельзя использовать запятые и скобки(скоро исправим)')


@dp.message_handler(commands=["about_photos"])
async def about_photos(message: types.Message):
    """ПРО ФОТО"""
    await message.answer('С помощью команды /photo вы можете загружать фотографии(пока что максимум одну) '
                         'на каждый предмет. Если у вас есть право на редактирование ДЗ, '
                         'то вы должны просто отправить фотограграфию и следовать дальнейшим инструкциям.'
                         'Пример использования схож с командой /add:'
                         '/photo верхняя понедельник математика '
                         'AgACAgIAAxkBAAIDk2OBCJY_fftOkOM2AAHknGQJ4W4K-wAC4soxGzkSCEh31A_XVBPQIgEAAwIAA3gAAysE')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photos_upload(message: types.Message):
    """ЗАГРУЗКА ФОТО"""
    if check_user_id(message.from_user.id):
        file_id = message.photo[-1].file_id
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Скопируйте следующее сообщение и вставьте после /photo <тип недели> <день недели> <предмет>'
        )
        await bot.send_message(chat_id=message.from_user.id, text=file_id)
    else:
        pass


@dp.message_handler(commands='photo')
async def photos_upload(message: types.Message):
    """ДОБАВЛЕНИЕ ФОТО"""
    if check_user_id(message.from_user.id):
        stroka = message.text.split()
        if stroka[1].lower() == 'верхняя':
            try:
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                PhotosDB_top.add_photo(f'"{week_day_ru}"', f'"{stroka[3]}"', f'"{stroka[4]}"')
                await message.answer('Вы успешно загрузили фотографию.')
            except Exception as ex:
                print(ex)
                await message.answer('Произошла ошибка.')
        elif stroka[1].lower() == 'нижняя':
            try:
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                PhotosDB_top.add_photo(f'"{week_day_ru}"', f'"{stroka[3]}"', f'"{stroka[4]}"')
                await message.answer('Вы успешно загрузили фотографию.')
            except Exception as ex:
                print(ex)
                await message.answer('Произошла ошибка.')
        else:
            await message.answer('Вы не выбрали тип недели.')
    else:
        pass


@dp.message_handler(commands=["add"])
async def add_hometask(message: types.Message):
    """ДОБАВЛЕНИЕ ДЗ"""
    if check_user_id(message.from_user.id):
        stroka = message.text.split()
        if stroka[1].lower() == 'верхняя':
            try:
                stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i > 3])
                stroka_with_subject = stroka[3].lower()
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                BotDB_top.add_homework_top(f'"{week_day_ru}"', f'"{stroka_with_subject}"', f'"{stroka_with_task}"')
                await message.answer('Вы успешно добавили задание.')
            except Exception as ex:
                print(ex)
                await message.answer('Произошла ошибка.')
        elif stroka[1].lower() == 'нижняя':
            try:
                stroka_with_task = ' '.join([el for i, el in enumerate(stroka) if i > 3])
                stroka_with_subject = stroka[3].lower()
                week_day_ru = (GoogleTranslator(source='ru', target='en').translate(stroka[2])).lower()
                BotDB_lower.add_homework_lower(f'"{week_day_ru}"', f'"{stroka_with_subject}"', f'"{stroka_with_task}"')
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
    """УДАЛЕНИЕ КЛАВИАТУРЫ"""
    await message.answer("Клавиатура скрыта.", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["hometask"])
async def hometask(message: types.Message):
    await message.answer("Выберите неделю", reply_markup=weeks_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'all_top_week')
async def all_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, BotDB_top.get_full_homework_top().replace('*', ','))


@dp.callback_query_handler(lambda call: call.data == 'all_lower_week')
async def all_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
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


@dp.callback_query_handler(lambda call: call.data == 'top_week_monday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, понедельник:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("monday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('monday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'top_week_tuesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, вторник:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("tuesday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('tuesday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'top_week_wednesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, среда:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("wednesday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('wednesday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'top_week_thursday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, четверг:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("thursday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('thursday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'top_week_friday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, пятница:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("friday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('friday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'top_week_saturday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Верхняя неделя, суббота:\n\n\n'
                                                  f'{BotDB_top.get_homework_top("saturday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_top.check_photos('saturday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


# Тут короче разделение недель, чтоб код понятней был


@dp.callback_query_handler(lambda call: call.data == 'lower_week_monday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, понедельник:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("monday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('monday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_tuesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, вторник:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("tuesday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('tuesday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_wednesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, среда:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("wednesday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('wednesday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_thursday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, четверг:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("thursday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('thursday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_friday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, пятница:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("friday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('friday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_saturday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, f'Нижняя неделя, суббота:\n\n\n'
                                                  f'{BotDB_lower.get_homework_lower("saturday")}'.replace('*', ','),
                           reply_markup=main_keyboard)
    for photo in PhotosDB_lower.check_photos('saturday'):
        if photo != '':
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo)


async def main():
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())
except Exception as ex:
    print(ex)
