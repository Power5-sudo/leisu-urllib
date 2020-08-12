#_*_ coding:utf-8_*_
"""

@Time:2020/8/12 17:53
@Author:Power5Bin
@File:resq.py
@IDE:PyCharm
@Email:75806318@qq.com

"""

import requests
import time
import scrapy
url = 'https://data.leisu.com/index-9021'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
res = requests.get(url,headers=headers)
print(res.text)
