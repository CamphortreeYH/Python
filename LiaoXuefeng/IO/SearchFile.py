# -*- coding: UTF-8 -*-

import os

def find_file(str,path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if str in file:
                print(os.path.join(root, file))

find_file("txt", "D:\\Automation\\LiaoXuefeng")
