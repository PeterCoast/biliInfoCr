# coding=utf-8
# 一键删除xml字幕文件
import os
import json
b_path = './file/'
print('开始清理字幕文件')
xml_list = [os.path.join(b_path, i) for i in os.listdir(b_path) if i.endswith('.xml')]
i = 1
while i <= len(xml_list):
    os.remove(xml_list[i-1])
    i+=1