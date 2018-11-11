import os
import win32gui

import requests
import json

import win32con

api_link = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
bing_host = 'https://www.bing.com'
file_dir = 'E:/BingPic/image/'


def open_url(url):
    response = requests.get(url)
    return response.content


def get_link(url):
    data = open_url(url)
    if data:
        json_data = json.loads(data.decode('utf-8'))
        images = json_data['images']
        res = {}
        for image in images:
            res[image['startdate']] = bing_host +image['url']
        return res


def check_path():
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


def save_image(url, file_path):
    content = open_url(url)
    with open(file_path, 'wb') as f:
        f.write(content)
    return file_path


def set_wallpaper(file_path):
    print('正在设置为壁纸...')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, file_path, 1 + 2)
    print('壁纸设置成功.')


def notify():
    pass


def main():
    check_path()
    res = get_link(api_link)
    if res:
        for k, v in res.items():
            file_path = save_image(v, file_dir + k + v[v.rfind("."):])
            set_wallpaper(file_path)


if __name__ == '__main__':
    main()
