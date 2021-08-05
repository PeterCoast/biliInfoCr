# coding=utf-8
import os

bvid = input('请输入视频BV号：')
b_path = './file/'

url = f'https://bilibili.com/video/{bvid}'
print('开始下载')
os.system(f'you-get -o {b_path} {url} --playlist')
