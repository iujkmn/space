#Скачивание и опубликование фоток космоса
Скачивание разных фоток космоса с сайта NASA а так же опубликование их в 
телеграм-канале "космо"

###Как установить
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) 
для установки зависимостей и установить зависимости.
Зависимости можно установить командой, представленной ниже.
Создайте бота у отца ботов.Создайте новый канал в Telegram.

Установите зависимости командой:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtuaienv/venv] для изоляции проекта.

###Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для получения необходимых изображений необходимо написать один из вариантов:
```
python get_EPIC_photos.py/get_APOD_photos.py/fetch_spacex_images.py
```

###Переменные окружения
Часть настроек проекта берётся из переменных окружения.
Переменные окружения-это переменные,значение которых присваиваются программе Python извне.
Чтобы их определить,создайте файл `.env` рядом с `main.py` и 
запишите туда данные в таком формате:ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:

```
API_KEY = "nasa-token"
TG_TOKEN = "bot-token"
CHAT_ID = "@chat_id"
```
Получить токен `API_KEY` можно на сайте [NASA](https://api.nasa.gov).
Получить токен `TELEGRAM_BOT_TOKEN` можно у отца ботов.
В описании канала получите название и положите в переменную `TG_CHAT_ID`.

###Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.