# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/10/16 0016 下午 14:45

names =["chang", "yang", "liu", "zhou", "wang"]

# 列表练习
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# hello = f"你好， {names[0]}"
# print(hello)

# 利用for循环遍历列表内容，实现每一个学员的问候。

#     print(hello)

# 把两个列表组合使用，调用遍历人名与交通工具的组合。
# 需要注意for循环的嵌套使用。
vehicles = ["bus", "plane", "steamboat", "train", "bicycle"]
# 使用zip()函数将两个列表中的元素一一对应地存储到一个字典中。字典的键是names列表中的元素，值是vehicles列表中的对应元素。
for i ,j in zip (names,vehicles):
    print(f"{i.title()}同学，喜欢{j.title()}出行。")

# 这样做会让第一个列表每个都循环一遍
# for i in names:
#     for j in vehicles:
#         print(f"{i.title()}同学，喜欢{j.title()}出行。")


