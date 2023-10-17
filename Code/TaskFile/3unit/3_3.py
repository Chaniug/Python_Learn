# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/10/17 0017 下午 16:27
# travels = ['bejing','wuhan','sichuan','guizhou','chongqing']
# # for i in travels:
# #     print(f"我想去{i}旅游")
# # sorted(travels)
# # print(travels)
# # sorted(travels,reverse=True)
# # print(travels)
# # travels.sort()
# # print(travels)
# travels.sort(reverse=True)
# print(travels)
# print(f"一共有{len(travels)}个可以旅游的地方")
city = ['bejing','wuhan','sichuan','guizhou','chongqing','shanghai']
rive = ['yellorive','changjiang','dongtinghu','haihei','nanhai']
country = ['china','usa','japan','france','germany','russia']
city.sort()
print(city)
sorted(city,reverse=True)
print(city)
rive.sort()
print(rive)
country.sort(reverse=True)
print(country)
travels = city + rive + country
print(travels)
country.reverse()
print(country)
print(len(travels))