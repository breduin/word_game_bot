Telegram бот для игры в слова.

В качестве базового кода использован [бот для учета финансовых расходов](https://github.com/alexey-goloburdin/telegram-finance-bot) 


В переменных окружения надо проставить API токен бота, а также адрес proxy и логин-пароль к ней.

`TELEGRAM_API_TOKEN` — API токен бота

## Запуск скрипта

```sh
python3 words_game.py
```

## Запуск с Docker

Предварительно заполните ENV переменные, указанные выше, в Dockerfile.

```
docker build -t wordsgame ./
docker run -d wordsgame
```
