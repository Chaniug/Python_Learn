# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2024/3/2 0002 下午 14:47

number1 = input("请输入第一个数字：")
number2 = input("请输入第二个数字：")
x = int(number1) + int(number2)
print("两个数字的和为：", x)

# # 简写该内容：
# .split()方法的用途是将一个字符串按照指定的分隔符分割成多个子字符串。
# 默认情况下，.split()方法使用空格作为分隔符。
# 使用.split()方法时，可以指定一个或多个分隔符。如果只有一个分隔符，可以不传递分隔符作为参数。
# 例如，对于字符串"hello world"，.split()方法的结果与.split(" ")相同。
# 如果需要使用非空字符作为分隔符，可以将分隔符放在字符串的第一个位置，或者在字符串的最后一个位置。
# 例如，对于字符串"hello,world"，.split(",")会返回["hello", "world"]，而.split(", ")会返回["hello", "world"]。
# 使用.split()方法时，可以指定一个最大分割次数，以避免无限分割。
# 例如，对于字符串"a.b.c.d"，.split(".", 2)会返回["a", "b.c.d"]，而.split(".")会返回["a", "b", "c", "d"]。

number3,number4 = input("请输入两个数字，并用空格隔开：").split()
print("两个数字的和为：", int(number3) + int(number4))