#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 20:05
# @Author  : Zhang Fei
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import urllib
# import urllib2
import re


# ----------- 回调函数进度 ------------#
def schedule(a, b, c):
    pre = 100.0 * a * b / c

    if pre > 100:
        pre = 100

    print('%.2f%%' % pre)


# ----------- 处理页面上的各种标签 -----------
class HTML_Tool:
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")

    # 用非 贪婪模式 匹配 任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")

    # 用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def Replace_Char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n    ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x


class xq_Spider:
    # 申明相关的属性
    def __init__(self, url):
        self.myUrl = url
        self.datas = []
        self.purl = []
        self.gurl = []
        self.myTool = HTML_Tool()
        print(u'已经启动爬虫，咔嚓咔嚓')

    # 初始化加载页面并将其转码储存
    def xq_info(self):
        # 读取页面的原始信息并将其从utf-8转码
        myPage = urllib.urlopen(self.myUrl).read().decode("utf-8")

        # 发布内容一共有多少页
        endPage = 2
        # 标题
        title = 'info'
        print(u'文件名：' + title)
        # 获取最终的数据
        self.save_data(self.myUrl, title, endPage)

    # 用来存储发布的内容
    def save_data(self, url, title, endPage):

        # 加载页面数据到数组中
        self.get_data(url, endPage)

        print('get data done')


        # 打开本地文件
        f = open(title + '.txt', 'a+')
        f.writelines(self.datas)
        f.close()

        self.download_pic()

        print(u'爬虫报告：文件已下载到本地并打包成txt文件')
        print(u'请按任意键退出...')
        input()

    # 获取页面源码并将其存储到数组中
    def get_data(self, url, endPage):
        url = url + '&page='
        for i in range(1, endPage + 1):
            print(u'爬虫报告：爬虫%d页正在加载中...' % i)
            myPage = urllib.urlopen(url + str(i)).read()

            # 将myPage中的html代码中所有url处理并存储到gurl里面
            self.deal_url(myPage.decode('utf-8'))

        print('url deal done')

        chinaurl = "http://www.china-seek.net/seek/"
        for i in self.gurl:
            infopage = urllib.urlopen(chinaurl + str(i)).read()
            self.deal_data(infopage.decode('utf-8'))

        print('data deal done')

    # 将编号从页面代码中抠出来
    def deal_url(self, myPage):
        myItems = re.findall('view/\?id=\d+', myPage)
        myPhoto = re.findall('photo/\d+.gif', myPage)
        for item in myItems:

            urlid = self.myTool.Replace_Char(item.replace("\n", "").encode('utf-8'))
            self.gurl.append(urlid + '\n')

        for item in myPhoto:

            urlpic = self.myTool.Replace_Char(item.replace("\n", "").encode('utf-8'))
            self.purl.append(urlpic + '\n')


    #从各个编号获取url
    def deal_data(self, infopage):

        infoItems = re.findall('class="r">(.*?)</div></li>', infopage, re.S)

        for item in infoItems:
            data = self.myTool.Replace_Char(item.replace("\n", "").encode('utf-8'))
            self.datas.append(data + '\n')

    def download_pic(self):
        chinaurl = "http://www.china-seek.net/seek/"
        picPath = './'

        for i in self.purl:
            picPage = urllib.urlopen(chinaurl + str(i)).read()
            print('fsfsfdsfsdfdsfsdfsd')
            print(picPage)
            pic = urllib.urlretrieve(picPage, picPath, schedule)

        # 打开本地文件
        f = open(i + '.txt', 'a+')
        f.writelines(self.pic)
        f.close()
