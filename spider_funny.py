# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup

def getHtmlCode(url):  #获取html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    url1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url1).read()
    page = page.decode('UTF-8')
    pageItems = page.find('div',class_='main')
    return pageItems

def getImg(page, localPath): #下载图片
    soup = BeautifulSoup(page, 'html.parser')
    imgList = soup.find_all('img')
    baseUrl = 'http://www.zbjuran.com'
    x = 0
    for imgUrl in imgList:
        print(u'正在下载：%s' % imgUrl.get('src'))
        urllib.request.urlretrieve(baseUrl+imgUrl.get('src'), localPath + '%d.gif' % x)
        x += 1

if __name__ == '__main__':
    url = 'http://www.zbjuran.com/quweitupian/'
    localPath = '/vagrant/php/img/'
    pageItems = getHtmlCode(url)


    getImg(page, localPath)
