# Processing of using scrapy(scrapy的基本使用步骤)

## Installation(安装)

```cmd
pip install scrapy
```

If you use Windows, you have another step:

```cmd
pip install pypiwin32
```

After installation, you should check whether you can use it:

```cmd
scrapy
```

you will get

```
Scrapy 1.7.2 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```

## Start your project

Open your terminal and 

```cmd
scrapy startproject quotetutorial
```

This will create a ```quotetutorial``` directory with following contents:

```
└─quotetutorial
    │  scrapy.cfg
    └─quotetutorial
        │  items.py
        │  middlewares.py
        │  pipelines.py
        │  settings.py
        │  __init__.py
        │
        ├─spiders
        │   __init__.py
```

## Your first spider

In your ```quotetutorial``` directory, you can use scrapy tool to generate your spider. You will see, ```quotes.py``` in your ```quotetutorial\spiders```.

```
scrapy genspider quotes quotes.toscrape.com
```

The explanation of above command:

- quotes: your spider name
- quotes.toscrape.com: the url you want to fetch data

## Run your spider

In order out your spider to work, you should go to ```quotetutorial``` directory.

```
scrapy crawl quotes
```
