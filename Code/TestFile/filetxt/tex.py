# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: chaniug
# @Email: chaniug@vip.qq.com
# @Time: 2024/6/17 上午10:12
# 定义输入文件和输出文件的名称
input_file = 'x.txt'
output_file = 'output.txt'

# 读取输入文件内容
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# 打开输出文件
with open(output_file, 'w') as outfile:
    for line in lines:
        # 去除每行的换行符
        line = line.strip()
        if line:  # 如果行非空
            # 写入原始网址
            outfile.write(line + '\n')
            # 写入加了"*."前缀的网址
            outfile.write('*.' + line + '\n')

print(f'处理完成，结果已写入 {output_file}')
