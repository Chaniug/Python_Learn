# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/6 0006 下午 17:03

print('\n'.join([' '.join([f"{j}x{i}={i*j}" for j in range(1, i + 1)]) for i in range(1, 10)]))