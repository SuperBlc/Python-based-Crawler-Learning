# Python Crawler Learning Notes(Python爬虫学习笔记)

## Directory Structure(目录结构)

- static(d)：some static files, for example, images and so on
- Chapterxx(f): Each notes begin with 'Chapter', and followed by chapter number and its name. Every *.ipynb is located at root directory.

## TODOS

- [x] Finish 'Chapter01-Fundamental-of-crewler'
- [x] Finish 'Chapter02-Fundamental-of-urlib'
- [ ] Finish 'Chapter03-Fundamental-of-requests'

## Environment

- Python 3.6
- requests 2.13.0
- selenium 3.3.1
- lxml 3.7.3
- pyquery 1.4.0
- beautifulsoap4 4.5.3
- PyMySQL 0.9.3
- pymongo 3.8.0
- redis 3.2.1

安装以上库：

```Python
pip install -r requirement.txt
```

## Needed packages and lib

- urllib, re ：Python内置的包
- requests
- ~~phantomjs~~(可以不用弹出浏览器窗口进行自动化测试。但新版的Chorme已不支持，可以使用([headless chrome](https://developers.google.com/web/updates/2017/04/headless-chrome))
- selenium ：用于驱动浏览器，常用于自动化测试, 如果要驱动chrome浏览器，需要下载对应的[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)。需要根据你使用的Chrome的版本来下载对应的ChromeDriver
  
  - 实例：Selenium+ Headless Chrome

```Python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
```

- lxml (用于解析xml和html)
- beautifulsoup4
- pyquery
- pymysql
- pymongo
- redis
- flask/django (服务器，设置代理)
- jupyter
