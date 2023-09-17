import requests
import os
from secondary_functions import get_extension, get_image
import datetime
from pathlib import Path
import argparse


def get_earth_images(folder_name, number_of_images,api_key):
    counter = 0
    url = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for launch_information in response.json():
        date = launch_information['date']
        name_of_image = launch_information['image']
        date = datetime.datetime.fromisoformat(date).strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name_of_image}.png"
        path = os.path.join(folder_name, f"{name_of_image}.png")
        if counter < number_of_images:
            get_image(url, path, params)
        counter += 1


def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии космоса с разных сайтов')
    parser.add_argument('number_of_images',
                        type=int,
                        default=4,
                        help='количество изображений')
    args = parser.parse_args()
    get_earth_images(folder_name, args.number_of_images,api_key)


if __name__ == '__main__':
    main()
