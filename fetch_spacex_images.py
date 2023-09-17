import requests
from secondary_functions import get_extension, get_image
from pathlib import Path
import argparse


def fetch_spacex_last_launch(launch_id, url):
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()
    if launch_id:
        urls = links['links']['flickr']['original']
    else:
        urls = []
        for link in links:
            if link['links']['flickr']['original']:
                urls += link['links']['flickr']['original']
    for index, photo_url in enumerate(urls):
        path = f"images/spacex_{index}{get_extension(photo_url)}"
        get_image(photo_url, path)


def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии космоса с разных сайтов')
    parser.add_argument('--id',
                        dest='launch_id',
                        default="5eb87d47ffd86e000604b38a",
                        help='id запуска')
    args = parser.parse_args()
    if args.launch_id:
        url = f"https://api.spacexdata.com/v5/launches/{args.launch_id}"
    else:
        url = "https://api.spacexdata.com/v5/launches/"
    fetch_spacex_last_launch(args.launch_id, url)


if __name__ == '__main__':
    main()
