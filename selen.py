#_*_ coding:utf-8_*_
"""

@Time:2020/8/12 0:19
@Author:Power5Bin
@File:selenium.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait



res = webdriver.Chrome()
header = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
res.get('https://data.leisu.com/index-9021')  # 通过get(url)
print(res.title)
time.sleep(5)
search = []
search = res.find_elements_by_class_name("data pd-8")
print(search[1])
#for x in search:
 #   header = x.find_element_by_class_name("v-a-m w-95 display-i-b")
 #   print(header)
#search.send_keys("test")
#search.send_keys(Keys.RETURN)

#print(search)
time.sleep(5)

res.close()