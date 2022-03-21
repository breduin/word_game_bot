"""Кастомные исключения, генерируемые приложением"""
from aiogram.utils.exceptions import BadRequest


class NoChar(BadRequest):
    """Нет слов, начинающихся с данной буквы."""
    pass
