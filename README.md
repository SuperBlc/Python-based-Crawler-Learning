# Python Crawler Learning Notes(Python爬虫学习笔记)

<!-- TOC -->
- [Python Crawler Learning Notes(Python爬虫学习笔记)](#python-crawler-learning-notespython%e7%88%ac%e8%99%ab%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0)
  - [Directory Structure(目录结构)](#directory-structure%e7%9b%ae%e5%bd%95%e7%bb%93%e6%9e%84)
  - [TODOS(做了以及将要做什么)](#todos%e5%81%9a%e4%ba%86%e4%bb%a5%e5%8f%8a%e5%b0%86%e8%a6%81%e5%81%9a%e4%bb%80%e4%b9%88)
  - [Environment(软件环境)](#environment%e8%bd%af%e4%bb%b6%e7%8e%af%e5%a2%83)
  - [Needed packages and lib(必需的包以及库)](#needed-packages-and-lib%e5%bf%85%e9%9c%80%e7%9a%84%e5%8c%85%e4%bb%a5%e5%8f%8a%e5%ba%93)
  - [Reference(A)](#referencea)
  - [Reference(B)](#referenceb)


## Directory Structure(目录结构)

PS: d-->direcotry, f-->file(*.ipynb)

- static(d)：some static files, for example, images and so on
- Chapterxx(f): Each notes begin with 'Chapter', and followed by chapter number and its name. Every *.ipynb is located at root directory.
- demo_file(d): Testing file for chapters.

## TODOS(做了以及将要做什么)

- [x] Finish ['Chapter01-Fundamental-of-crewler'](./Chapter01-Fundamental-of-crewler.ipynb)
- [x] Finish ['Chapter02-Fundamental-of-urlib'](./Chapter02-Fundamental-of-urlib.ipynb)
- [x] Finish ['Chapter03-Fundamental-of-requests'](./Chapter03-Fundamental-of-requests.ipynb)
- [x] Finish ['Chapter04-Fundamental-of-regular-expression'](./Chapter04-Fundamental-of-regular-expression)
- [x] Finish ['Chapter05-Fundamental-of-beautifulsoup'](./)
- [x] Finish ['Chapter06-Fundamental-of-pyquery'](./Chapter06-Fundamental-of-pyquery.ipynb)
- [ ] Finish ['Chapter07-Fundamental-of-selenium'](./Chapter07-Fundamental-of-selenium.ipynb)
  
## Environment(软件环境)

- Python 3.6
- requests 2.13.0
- selenium 3.3.1
- lxml 3.7.3
- pyquery 1.4.0
- beautifulsoap4 4.5.3
- PyMySQL 0.9.3
- pymongo 3.8.0
- redis 3.2.1
- jupyterlab

安装以上库：

```bash
pip install -r requirement.txt
```

## Needed packages and lib(必需的包以及库)

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
- jupyterlab

## Reference(A)

1. [崔庆才--Python3爬虫](https://cuiqingcai.com/5052.html)
2. [《Python3网络爬虫开发实战》作者：崔庆才](https://germey.gitbooks.io/python3webspider/content/)

## Reference(B)

1. Python, [Python官网](https://www.python.org/)
2. Jupyter-lab, [Jupyter官网](https://jupyter.org/install.html)
3. urllib, [urllib文档](https://docs.python.org/3.6/library/urllib.html#module-urllib)
4. requests, [requests文档](https://2.python-requests.org/en/master/)
5. re, [re模块文档](https://docs.python.org/3.6/library/re.html#module-re)
6. RegExr, [测试、学习regex](https://regexr.com/)
7. BeautifulSoup, [轻松提取网页数据--BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)
8. PyQuery, [像Jquery一样提取网页数据--PyQuery](https://pyquery.readthedocs.io/en/latest/)
9. Selenium, [自动化测试工具--Selenium官网](https://www.seleniumhq.org/)
10. ChromeDriver, [Chrome驱动](https://sites.google.com/a/chromium.org/chromedriver/)
11. MySQL, [关系型数据库-MySQL5.7下载页](https://dev.mysql.com/downloads/mysql/5.7.html#downloads)
12. PyMySQL, [Python版本的MySQL操作库--PyMySQL文档](https://pymysql.readthedocs.io/en/latest/)
13. MongoDB, [非关系型数据库--MongoDB下载](https://www.mongodb.com/download-center)
14. pymongo, [操作MongoDB的Python库](https://api.mongodb.com/python/current/)
15. Redis, [key-value存储、操作为原子操作、数据缓存在内存中的数据库系统--Redis](https://redis.io/)
16. redis, [操作Redis的python库](https://github.com/andymccurdy/redis-py)
17. Flask, [Python微型后端框架--Flask](https://palletsprojects.com/p/flask/)
18. DJango, [Python后端框架--Django](https://www.djangoproject.com/)
19. HTML/CSS/JavaScript, 前端基本知识，[MDN](https://developer.cdn.mozilla.net/en-US/docs/Web)，[W3School-英文](https://www.w3schools.com/)、[W3School-中文](https://www.w3school.com.cn/)