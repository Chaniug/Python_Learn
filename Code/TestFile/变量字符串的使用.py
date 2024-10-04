ad_name = 'adidas'
bl_name = 'blaclash'

# 新版本支持调用f字符串，能够自动的调用变量的内容，引用变量的内容。

full_name = f"{ad_name} {bl_name},欢迎你们"
print(full_name)    
print(f'{full_name.title()}')  # 首字母大写
# \t实现空格
print( "\t" f'{full_name.upper()}')  # 全部大写


null_name = '  python is my love !   '
print(null_name.lstrip()) # 去除左边的空格
print(null_name.rstrip())  # 去除右边的空格
print(null_name.strip())  # 去除两边的空格

web_name = 'https://www.baidu.com'
print(web_name.removeprefix('https://'))  # 拆分字符串
