#_*_ coding:utf-8_*_
"""

@Time:2020/8/13 2:49
@Author:Power5Bin
@File:requests-test.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
import json
from urllib.request import urlopen



url=urlopen('https://api.namitiyu.com/v1/football/match/detail?sid=3421713')
res = json.loads(url.read().decode('utf-8'))
res = json.dumps(res, ensure_ascii=False)
print(res) 


#将爬取的内容写入xxx.html文件
with open('detail.html', 'w', encoding='utf-8') as f:
    f.write(res)
