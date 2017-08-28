# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup

def getHtmlCode(url):  #encoding:utf-8
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    url1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url1).read()
    return page

def getImg(page, localPath):
    soup = BeautifulSoup(page, 'html.parser')
    imgList = soup.find_all('img')
    baseUrl = 'http://www.zbjuran.com'
    x = 0
    for imgUrl in imgList:
        print(u'正在下载：%s' % imgUrl.get('src'))
        urllib.request.urlretrieve(baseUrl+imgUrl.get('src'), localPath + '%d.gif' % x)
        x += 1

if __name__ == '__main__':
    url = 'http://www.zbjuran.com/dongtai/'
    localPath = '/vagrant/php/img/'
    page = getHtmlCode(url)
    getImg(page, localPath)
