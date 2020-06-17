#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:31
# @Author  : Zhang Fei
# @Site    :
# @File    : spide.py
# @Software: PyCharm

# import requests
# import re
#
# key = '食品'
# url = 'https://b2b.baidu.com/s?q=' + key
# data = requests.get(url).text
# tit = '"fullName":"(.*?)"'
# alltit = re.compile(tit, re.S).findall(data)
# for item in alltit:
#     print('标题: '+eval('u"' + str(item) + '"'))
#     # eval 将字符串str当成有效的表达式子来求值并返回计算结果
#    # print('--------------')


import urllib.request
import re
import os
import urllib


def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')


def get_img(html):
    reg = r'https://[^\s]*?\.jpg'
    imgre = re.compile(reg)  # 转换成一个正则对象
    imglist = imgre.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    x = 0        # 声明一个变量赋值
    path = 'D:\\lianxi\\mypic\\test'  # 设置图片的保存地址
    if not os.path.isdir(path):
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'  # 保存在test路径下
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
        x = x + 1
        print('图片开始下载，注意查看文件夹')
    return imglist


html_b = get_html("https://tieba.baidu.com/p/6055320747")  # 获取该网页的详细信息
print(get_img(html_b))  # 从网页源代码中分析下载保存图片
