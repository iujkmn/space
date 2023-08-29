import telegram
import os
import time
import random
import argparse

def post_photo(secs):
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    paths = []
    counter = 0
    for address, dirs, files in os.walk("images"):
        for name in files:
            path = os.path.join(address, name)
            paths.append(path)
    while True:
        if counter >= len(paths):
            random.shuffle(paths)
        for path in paths:
            bot.send_document(chat_id="@cosmo_image",
                              document=open(path, 'rb'))
            counter += 1
            time.sleep(secs)

def main():
    parser = argparse.ArgumentParser(
        description='Публикует фотографии космоса в телеграм-канал')
    parser.add_argument('secs',
                        type=int,
                        default=14400,
                        help='количество секунд')
    args = parser.parse_args()
    post_photo(args.secs)


if __name__ == '__main__':
    main()
