import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from keyboards import weeks_keyboard, top_week_keyboard, lower_week_keyboard, main_keyboard
from clas import BotDB

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5943456648:AAHnaCeOanZYMK4T8mKHlRIg267Bb2_C6PA")
dp = Dispatcher(bot)

BotDB = BotDB('top_week.db')


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Вас приветствует бот, созданный, чтобы говорить вам ваше домашнее задание. "
                         "Введите /help , чтобы узнать функционал бота и открыть клавиатуру с командами.")


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer("Команды: /hometask", reply_markup=main_keyboard)


@dp.message_handler(commands=["remove_keyboard"])
async def help(message: types.Message):
    await message.answer("Клавиатура скрыта.", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["hometask"])
async def hometask(message: types.Message):
    await message.answer("Выберите неделю", reply_markup=weeks_keyboard)


@dp.callback_query_handler(text='top_week')
async def top_week_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день недели(верхняя)', reply_markup=top_week_keyboard)


@dp.callback_query_handler(text='lower_week')
async def lower_week_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите день недели(нижняя)', reply_markup=lower_week_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_monday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, BotDB.monday(), reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_tuesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'п', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_wednesday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'п', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_thursday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'п', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_friday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'п', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'top_week_saturday')
async def dz_top(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'п', reply_markup=main_keyboard)


# Тут короче разделение недель, чтоб код понятней был


@dp.callback_query_handler(lambda call: call.data == 'lower_week_monday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_tuesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_wednesday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_thursday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_friday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'lower_week_saturday')
async def dz_lower(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'нижняя', reply_markup=main_keyboard)


@dp.message_handler(commands=["lower_week"])
async def help(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=lower_week_keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())