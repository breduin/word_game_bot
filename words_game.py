"""Telegram бот для игры в слова"""
from itertools import groupby
import logging
import os
import random

from aiogram import Bot, Dispatcher, executor, types

import exceptions


logging.basicConfig(level=logging.INFO)


API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WORDS_FILENAME = 'singular.txt'
MAX_NUM_WORDS_WITH_CHAR = 3

class WordIssue:
    """Получить слова из списка по одному."""
    def __init__(self, words):
        self._words = words
        alphabet = sorted(
            {k for k, g in groupby(words, key=lambda x: x[0])}
            )
        self._words_by_first_char = {}
        for char in alphabet:
            words_starting_with_char = [word for word in self._words if word.startswith(char)]
            self._words_by_first_char[char] = random.choices(
                words_starting_with_char, k=MAX_NUM_WORDS_WITH_CHAR
                )


    def pick(self, last_char):
        last_char = last_char.lower()
        if last_char not in self._words_by_first_char:
            raise exceptions.NoChar()
        try:
            return self._words_by_first_char[last_char].pop()
        except IndexError:
            raise LookupError(f'Слова на \"{last_char}\" закончились!')

    def __call__(self):
        return self.pick()


with open(WORDS_FILENAME, 'r', encoding='utf-8') as words_file:
    words = words_file.read().split('\n')


words_queue = WordIssue(words)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer("Поиграем в слова? Введи слово.")


@dp.message_handler()
async def echo(message: types.Message):
    """Отправить эхо-сообщение"""
    last_char = message.text[-1]
    try:
        answer_message = words_queue.pick(last_char)
    except LookupError:
        answer_message = f'Я больше слов на \"{last_char}\" не знаю ... Твоя победа!'
    except exceptions.NoChar():        
        f'Слов на \"{last_char}\" нет! Введи другое слово.'

    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)