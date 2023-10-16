# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/5 0005 上午 09:24
import random

empolyes = []
for i in range(1, 301):
    empolyes.append(f"员工:{i}")

# third_winner =random.sample(empolyes,20)
# print(third_winner)
# 奖池等级
staff = [30, 6, 3]
gift = ['5斤苹果', '手机', '5日游']
# 控制等级输出
for j in range(3):
    winner_list = random.sample(empolyes, staff[j])
    # print(winner_list)
    print(f"恭喜获得{3 - j}等奖{gift[j]}是：", winner_list)
    # 用for循环控制删除掉或将的
    for winner in winner_list:
        empolyes.remove(winner)
    print(f"还剩{len(empolyes)}没有中奖")
