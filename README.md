# Python 学习记录
## TODO 
### 1.pip使用
### 2.文本爬虫编写
### 3.图片爬虫

-----------------------------
# 使用Python 国内镜像
### http://pypi.douban.com/simple
如果想手动指定源，可以在pip后面跟-i 来指定源，比如用豆瓣的源来安装web.py框架：
pip install web.py -i http://pypi.douban.com/simple
要配制成默认的话，需要创建或修改配置文件（linux的文件在~/.pip/pip.conf，windows在%HOMEPATH%\pip\pip.ini），修改内容为：
### code:
```
[global]
index-url = http://pypi.douban.com/simple
```