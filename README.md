# 简介

browser_useragent 库共包含246个浏览器请求头

参考fake_useragent库，对其进行了简化，解决网络不好文件下载失败的问题

chrome, opera, firefox, safari, internetexplorer


来源： fake_useragent:
http://d2g6u4gh6d9rq0.cloudfront.net/browsers/fake_useragent_0.1.9.json


# 快速开始

安装

```
pip install browser_useragent
```

使用

```python

>>from browser_useragent import get_user_agent

>>get_user_agent()

>>'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0'

```