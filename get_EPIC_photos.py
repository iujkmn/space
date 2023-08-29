import requests
import os
from secondary_functions import get_extension, get_image
import datetime
from pathlib import Path
import argparse


def get_EPIC(folder_name, number_of_images):
    counter = 0
    url = "https://api.nasa.gov/EPIC/api/natural/image"
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for index in response.json():
        date = index['date']
        name_of_image = index['image']
        date = datetime.datetime.fromisoformat(date).strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name_of_image}.png"
        path = os.path.join(folder_name, f"{name_of_image}.png")
        if counter < number_of_images:
            get_image(url, path, params)
        counter += 1


def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Скачивает фотографии космоса с разных сайтов')
    parser.add_argument('number_of_images',
                        type=int,
                        help='количество изображений')
    args = parser.parse_args()
    get_EPIC(folder_name, args.number_of_images)


if __name__ == '__main__':
    main()