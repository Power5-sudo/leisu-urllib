#_*_ coding:utf-8_*_
"""

@Time:2020/8/11 19:36
@Author:Power5Bin
@File:001.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
import requests
import urllib
import json
import re
from urllib.request import urlopen
from pprint import pprint

header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
#request = urllib.request.Request('https://data.leisu.com/index-9021',headers=header)

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应

#response = urllib.request.urlopen(request)
#response.encoding = ('utf-8')
#html = response.read()

#获取HTTP请求响应码,200：表示成功返回；4开头：服务器页面出错；5开头：服务器问题，通常是应用服务器和数据库没启好

#print(html)







url = 'https://data.leisu.com/index-9021'
res = requests.get(url,headers=header)
res.encoding = 'utf=8'
print(res.text)

#def site_web(url):
#   url = urlopen('https://data.leisu.com/index-9021')

  #  try:
   #     res =