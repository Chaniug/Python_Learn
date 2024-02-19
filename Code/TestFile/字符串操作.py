# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2024/2/19 0019 下午 17:15

s = "hellom, chen"
# #在Python中，字符串是一个字符序列。要定义一个字符串，可以使用单引号（''）或双引号（""）来括起字符。例如：
# ```python
# string1 = 'Hello, World!'
# string2 = "Python is fun!"
# ```
# 在这个例子中，`string1`和`string2`都是字符串。

age = 18
work = "student"
my = f"你好{s}，{age}{work}"
print("que" in work) # 判断字符串中是否包含某个字符串
print(work[0:4]) #字符串截取
print(work[::-1]) #字符串翻转
print("*"*30) #字符串的拼接操作
print(len(work))
print(my)
