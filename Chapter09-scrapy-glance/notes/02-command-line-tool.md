# Scrapy command line tool

scrapy的命令行工具

文档：https://docs.scrapy.org/en/latest/topics/commands.html


## Createing projects 创建工程

使用scrapy的第一件事情就是用```scrapy```命令创建 Scrapy 工程：

```
scrapy startproject 工程名 [工程目录]
```

PS: 可选参数 '工程目录' --> 可以指定工程目录，默认是在当前目录下创建工程目录

下一步就是进入工程目录，再使用```scrapy```命令来管理和控制工程

## Controlling projects

在工程目录中使用```scrapy```来管理项目

如：创建spider

```
scrapy genspider example https://xyz.nn
```

- 全局命令（可不在项目下使用）-- work without an active Scrapy project
  - startproject
  - genspider：生成spider，可以指定模板生成spider
  - settings
  - runspider
  - shell：进入命令行交互模式
  - fetch：获取网页源代码
  - view
  - version
```
(web-bug) λ scrapy version -v
Scrapy       : 1.7.2
lxml         : 3.7.3.0
libxml2      : 2.9.4
cssselect    : 1.0.3
parsel       : 1.5.1
w3lib        : 1.20.0
Twisted      : 19.2.1
Python       : 3.6.0 |Continuum Analytics, Inc.| (default, Dec 23 2016, 11:57:41) [MSC v.1900 64 bit (AMD64)]
pyOpenSSL    : 19.0.0 (OpenSSL 1.1.1c  28 May 2019)
cryptography : 2.7
Platform     : Windows-10-10.0.18362-SP0
```
- 仅在项目下使用的命令 -- only work fron inside a Scrapy project
  - crawl：运行spider
  - check：检查语法错误
  - list：列出项目中所有的spider的名称
  - edit
  - parse
  - bench 