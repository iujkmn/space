from secondary_functions import get_extension, get_image
import requests
from pathlib import Path
import argparse
import os


def get_astronomy_picture(digit,api_key):
    url = "https://api.nasa.gov/planetary/apod?"
    params = {
        "api_key": api_key,
        "count": str(digit)
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    links = []
    for number in range(digit):
        url = response.json()[number]['url']
        links.append(url)
    for index, url in enumerate(links):
        path = f"images/nasa_apod{index}{get_extension(url)}"
        get_image(url, path, params)


def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    api_key = os.environ['API_KEY']
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии космоса с разных сайтов')
    parser.add_argument('digit',
                        type=int,
                        default=4,
                        help='количесто изображений')
    args = parser.parse_args()
    get_astronomy_picture(args.digit,api_key)


if __name__ == '__main__':
    main()
