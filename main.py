import telegram
import os
import time
import random
import argparse

def post_photos(secs, token, chat_id)::
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=token)
    while True:
        files = os.listdir("images")
        random.shuffle(files)
        for file in files:
            path = os.path.join("images", file)
            with open(path,"rb") as document:
                bot.send_document(chat_id="@cosmo_image",
                                  document=document)
            time.sleep(secs)

def main():
    chat_id = os.environ['TG_CHAT_ID'] 
    token = os.environ['TG_TOKEN']
    parser = argparse.ArgumentParser(
        description='Публикует фотографии космоса в телеграм-канал')
    parser.add_argument('secs',
                        type=int,
                        default=14400,
                        help='количество секунд')
    parser.add_argument('--chat_id',
                        dest='chat_id',
                        default=chat_id,
                        help='чат айди')
    args = parser.parse_args()
    post_photos(args.secs, token, args.chat_id)


if __name__ == '__main__':
    main()
