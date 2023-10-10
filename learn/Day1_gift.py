# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/4 0004 下午 17:08
import random
employes = list(range(1,301))
third_gift_winner = random.sample(employes,30)
for winner in third_gift_winner:
    employes.remove(winner)
print("获得3等奖的员工是：")
for winner in third_gift_winner:
    print(winner)

