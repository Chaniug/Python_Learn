# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/6 0006 上午 10:01

import random
empolys_list =[]
gift = [30,6,3]
for i in range(300):
    empolys_list.append(f"员工{i}")

for j in range(3):
    winner_list = random.sample(empolys_list,gift[j])
    print(f"恭喜中了{3-j}等奖了：",winner_list)
    for win in winner_list:
        empolys_list.remove(win)
    print(f"还剩{len(empolys_list)}没有中奖")


