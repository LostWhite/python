# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import json

def getHtmlCode(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    url1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url1).read()
    page = page.decode('UTF-8')
    return page

def getNews(page):
    soup = BeautifulSoup(page, 'html.parser')
    newsList = soup.find('div',id='geek_list').find_all('dl',class_='geek_list')
    x=0
    dictionary = {}
    for news in newsList:
        print(u'保存文章：%s' % news.find('a',class_='title').string)
        dictionary[news.find('a',class_='title').string] = news.find('a',class_='title')['href']
    return json.dumps(dictionary)

def saveFile(fileData):
    file = open("/vagrant/php/python/csdn.json","w")
    file.write(fileData)
    file.close()

if __name__ == '__main__':
    url = 'http://geek.csdn.net/'
    localPath = '/vagrant/php/'
    page = getHtmlCode(url)
    jsonData = getNews(page)
    saveFile(jsonData)