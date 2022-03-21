
FROM python:3.10

WORKDIR /home

ENV TELEGRAM_API_TOKEN=""

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY *.py ./
COPY *.txt ./
RUN pip install -U pip && pip install -r requirements.txt

ENTRYPOINT ["python", "words_game.py"]