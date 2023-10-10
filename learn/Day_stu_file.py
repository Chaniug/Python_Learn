# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/4 0004 下午 12:21

import random

# 定义员工列表
employees = list(range(1, 301))

# 第一次抽奖：3等奖
print("第一次抽奖：三等奖【5斤苹果】")
third_prize_winners = random.sample(employees, 30)
for winner in third_prize_winners:
    employees.remove(winner)
print("正在抽取中----")
# 打印中奖名单
print("获得三等奖的员工编号：")
for winner in third_prize_winners:
    print(winner)

# 第二次抽奖：2等奖
print("第二次抽奖：二等奖【苹果14手机】")
second_prize_winners = random.sample(employees, 6)
for winner in second_prize_winners:
    employees.remove(winner)
print("正在抽取中----")
# 打印中奖名单
print("\n获得二等奖的员工：")
for winner in second_prize_winners:
    print(winner)
# 第三次抽奖：1等奖
print("第三次抽奖：一等奖【豪华5日游】")
first_prize_winners = []
for i in range(3):
    input("【点击抽取】第{}位获得一等奖的幸运员工：".format(i + 1))
    winner = random.choice(employees)
    first_prize_winners.append(winner)
    employees.remove(winner)
    print("中奖者：", winner)
print("一等奖抽奖结束\n")
#打印中奖名单
print("\n获得一等奖的员工编号：")
for winner in first_prize_winners:
    print(winner)