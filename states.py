from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class WriteHomeworkTop(StatesGroup):
    add_text = State()
    add_photo = State()


class WriteHomeworkLower(StatesGroup):
    add_text = State()
    add_photo = State()


storage = MemoryStorage()