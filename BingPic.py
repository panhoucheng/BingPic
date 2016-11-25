# -*- coding: utf-8 -*-

import os
import urllib.request
import datetime

COLLECTION_DIR = 'D://bingPic/'

def collect_bing_picure():
   pic_url = None
   f = urllib.request.urlopen('http://cn.bing.com/')
   page_source = str(f.read())

   if page_source.find('s.cn.bing.net') >= 1:
      pre_url = page_source.split('s.cn.bing.net')[1]
      clean_url = pre_url.split('.jpg')[0].replace('\\', '')
      pic_url = 'http://s.cn.bing.net%s.jpg' % clean_url
      print(pic_url)

   if pic_url is not None:
      nowa_time = datetime.datetime.now().strftime('%Y%m%d')

      if not os.path.exists(COLLECTION_DIR):
         os.mkdir(COLLECTION_DIR)
      urllib.request.urlretrieve(pic_url, COLLECTION_DIR + nowa_time + '.jpg')

      print('download successful')

if __name__ == '__main__':
   collect_bing_picure()