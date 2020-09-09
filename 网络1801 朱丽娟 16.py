# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from urllib import request
url="https://www.ivsky.com/bizhi/yingshi/"
re_jpg=re.compile(r'<img src="(.*?\.jpg)"')
user_agent='Chrome/4.0(compatible;MAIE 5.5;Windows NT)'
req=request.Request(url,headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT'})
response=request.urlopen(req)
html=response.read().decode('utf-8')
img_list=re_jpg.findall(html)
n=0
for i  in img_list:
    request.urlretrieve("https:"+i,"%s.jpg"%n)
    print('download %s'%i)
    n+=1



