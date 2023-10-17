# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/10/17 0017 上午 09:41

guest_list = ['流川枫', '赤井里奈',  '中井龙一']
# 遍历列表邀请参加活动
# for i in guest_list:
#     print(f"欢迎{i}参加活动！")
# print(f"{guest_list[2]}无法参加此次活动")
# 修改列表内容，可以采用列表元素定位。或者使用append()方法
# # guest_list[2] = '神里绫华'
guest_list.append('神里绫华')
# 还可以使用insert()方法 insert(x,"值")
# guest_list.insert(2, '神里绫华')
for f in guest_list:
    print(f"欢迎【{f}】参加活动！")

print("\n有一个更大的餐桌！大家请移步！")

# 进阶部分，将两个列表合并成一个big列表
# 方法1
# list2 = [None] * len(list1)  # 创建一个长度和list1相同的空列表
#
# for i in range(len(list1)):
#     list2[i] = list1[i]  # 将list1中的元素逐个添加到list2中
#
# big_guest =[None] * len(guest_list)
# for s in range(len(guest_list)):
#     big_guest[s] = guest_list[s]
#
# 方法2
# # 可以使用for提取旧列表的内容，再使用append方法添加到新列表
# # for e in guest_list:
# #     big_guest.append(e)
#

# 方法3
# 简洁便于阅读 元素直接提取放到新列表中，跟方法2实现的效果是一样的
big_guest = [item for item in guest_list]
#
big_guest.insert(0, '上条当麻')
big_guest.insert(1,'上原亚衣')
big_guest.append('上原步美')

# 拓展知识
# 元素升降序排列的方法
# 列表元素升序排列 sort()列表元素升序排列
# big_guest.sort()
# # 降序排列
# big_guest.sort(reverse=True)

print(big_guest)
for g in big_guest:
    print(f"欢迎【{g}】来到新餐桌参加")

# 使用pop()以及del语句缩减列表
# 使用remove移除列表的元素
big_poped1 = big_guest.pop()
big_poped2 = big_guest.pop(2)
big_poped3 = big_guest.pop(3)
print("\n抱歉，临时有事无法参加:",big_poped1,big_poped2,big_poped3)
for k in big_guest:
    print(f"欢迎【{k}】继续参加宴会！")

del big_guest[1]
del big_guest[0]
big_guest.remove('神里绫华')
big_guest.remove('赤井里奈')
print(big_guest)
print(len(big_guest))