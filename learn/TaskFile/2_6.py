names = "\t akie \n"
print(names)
# .rsplit()删除末尾的空行
names_1 = f"{names.rsplit()}"
print(names_1)

# .lstrip()用于从字符串的开头删除空白字符。它返回一个新的字符串，其中开头所有的空白字符都被删除。
names_2 = f"{names.lstrip()}"
print(names_2)

# names.strip()用于删除字符串开头和结尾的空白字符。它返回一个新的字符串，其中开头和结尾的空白字符都被删除。
names_3 = f"{names.strip()}"
print(names_3)