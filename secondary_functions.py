from urllib.parse import urlsplit
import urllib.parse
import requests
import os
from pathlib import Path


def get_image(url, path, params):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    str_url = urllib.parse.unquote(url)
    url = urlsplit(str_url).path
    return (os.path.splitext(url))[1]


def main():
    folder_name = "images"
    Path(folder_name).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    main()
