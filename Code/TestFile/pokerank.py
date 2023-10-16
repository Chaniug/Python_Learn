# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2023/7/5 0005 上午 11:01

import random
suits = ['方片','梅花','红桃','黑桃']
faces = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']

# 生成一副有52张牌的扑克牌
deck = [suit + face for suit in suits for face in faces]

# 模拟洗牌
random.shuffle(deck)

# 用户选一张牌
while True:
    user_card = input("请选择一张牌（例如：红桃A）：")
    if user_card in deck:
        break
    else:
        print("无效的牌，请重新选择。")

# 电脑随机抽取一张牌
computer_card = random.choice([card for card in deck if card != user_card])

# 提取牌面和花色等级
user_face = user_card[2:]
user_suit = user_card[:2]
computer_face = computer_card[2:]
computer_suit = computer_card[:2]

# 显示用户选择的牌面和花色
print("你选择的牌是：", user_card)
print("电脑选择的牌是：", computer_card)

# 判断牌面大小
if faces.index(user_face) > faces.index(computer_face):
    print("你赢了!")
elif faces.index(user_face) < faces.index(computer_face):
    print("你输了...")
else:
    # 牌面相同，判断花色等级
    if suits.index(user_suit) > suits.index(computer_suit):
        print("你赢了!")
    else:
        print("你输了...")


