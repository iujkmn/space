import requests
from secondary_functions import get_extension, get_image
from pathlib import Path
import argparse



def fetch_spacex_last_launch(launch_id):
    url = "https://api.spacexdata.com/v5/launches"
    params = {"id": launch_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    urls = response.json()[24]['links']['flickr']['original']
    for index, url in enumerate(urls):
        path = f"images/spacex_{index}{get_extension(url)}"
        get_image(url, path, params)

def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии космоса с разных сайтов'
    )
    parser.add_argument('--id', dest='launch_id', default="5eb87d47ffd86e000604b38a", help='id запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == '__main__':
    main()
