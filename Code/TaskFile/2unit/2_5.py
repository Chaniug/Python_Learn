# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/10/11 0011 下午 16:39
famous_person = "albert einstein"
message = '"A person who never made amistake never tried anything new ."'
# capitalize()是一个字符串方法，用于将字符串中的所有单词的首字母转换为大写。它不会改变字符串中其他字母的大小写。
message_find = f'{famous_person.title()} said: {message}'
print(message_find)