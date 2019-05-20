# -*- coding: utf-8 -*-

__author__ = 'xua'

import json

# For python 3.x
from html.parser import HTMLParser


# 定义HTMLParser的子类,用以复写HTMLParser中的方法
class MyHTMLParser(HTMLParser):

    # 构造方法,定义data数组用来存储html中的数据
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    # 覆盖starttag方法,可以进行一些打印操作
    def handle_starttag(self, tag, attrs):
        pass
        # print("Start Tag: ",tag)
        # for attr in attrs:
        #   print(attr)

    # 覆盖endtag方法
    def handle_endtag(self, tag):
        pass

    # 覆盖handle_data方法,用来处理获取的html数据,这里保存在data数组
    def handle_data(self, data):
        if data.count('\n') == 0:
            self.data.append(data)


# 读取本地html文件.(当然也可以用urllib.request中的urlopen来打开网页数据并读取,这里不做介绍)
htmlFile = open("TFS.htm", 'r', encoding='UTF-8')
content = htmlFile.read()

# 创建子类实例
parser = MyHTMLParser()

# 将html数据传给解析器进行解析
parser.feed(content)

# 对解析后的数据进行相应操作并打印
for item in parser.data:
    if item.startswith("{\"columns\""):
        payloadDict = json.loads(item)
        list = payloadDict["payload"]["rows"]
        for backlog in list:
            if backlog[1] == "Product Backlog Item" or backlog[1] == "Bug":
                print(backlog[2], "       Point: ", backlog[3])