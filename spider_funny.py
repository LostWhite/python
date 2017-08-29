# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import os
import random


def getHtmlCode(url):  # 获取html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    url1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url1).read()
    return page


def getItem(items, localPath, baseUrl):  # 获取item
    for item in items:
        print(item.find('b'))
        if item.find('b') != None:
            print('获取图片文件: %s', item.find('b').string)
            savePath = localPath + item.find('b').string
            if not os.path.exists(savePath):
                os.mkdir(savePath)
            getImg(baseUrl + item.find('h3').find('a')['href'], savePath)


def getImg(url, savePath):  # 下载图片
    page = getHtmlCode(url)
    soup = BeautifulSoup(page, 'html.parser')
    imgList = soup.find('div', class_='page').find_all("li")
    saveImg(url,savePath)
    for img in imgList[3:len(imgList) - 1]:
        if img.find('a') != '':
            imgUrl = img.find('a')['href']
            front = os.path.split(url)
            imgUrl = front[0] + "/" + imgUrl
            saveImg(imgUrl, savePath)


def saveImg(imgUrl, savePath):
    page = getHtmlCode(imgUrl)
    soup = BeautifulSoup(page, 'html.parser')
    baseUrl = 'http://www.zbjuran.com'
    finUrl = baseUrl + soup.find('div', class_='text').find('img')['src']
    p = soup.find('div', class_='text').find_all('p')[2]
    fileName = p.string.replace('\r', '').replace('\n', '').replace('\t', '')
    print(fileName)
    urllib.request.urlretrieve(finUrl, savePath + '/' + '%s.jpg' % fileName)


if __name__ == '__main__':
    url = 'http://www.zbjuran.com/quweitupian/'
    localPath = '/vagrant/php/img/'
    baseUrl = 'http://www.zbjuran.com'
    page = getHtmlCode(url)
    soup = BeautifulSoup(page, 'html.parser')
    pageItems = soup.find('div', class_='main').find_all('div', class_='item')
    getItem(pageItems, localPath, baseUrl)
