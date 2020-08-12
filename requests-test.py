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


#headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
#response = requests.get(url='https://api.namitiyu.com/v1/football/match/detail?sid=3421713',headers=headers)
#response.encoding = 'utf-8'
url=urlopen('https://api.namitiyu.com/v1/football/match/detail?sid=3421713')
res = json.loads(url.read().decode('utf-8'))
res = json.dumps(res, ensure_ascii=False)
print(res)  # <Response [200]>
# 返回响应状态码
# 200
# 返回响应文本
# print(response.text)
# <class 'str'>

#将爬取的内容写入xxx.html文件
with open('detail.html', 'w', encoding='utf-8') as f:
    f.write(res)