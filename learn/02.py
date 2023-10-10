"""
使用变量保存数据并进行算术运算

Version: 0.1
Author: chaniug
"""
print("这么帅的男人就是我 \n" *10 )
student_list=['zhanghua ','lixue','huichun','iuty']
student_list.insert(3,'sdsda')
student_list[0] = 'chen'
student_list.append('Alex')
student_list.remove('chen')
student_list.append('chen')
for stu in student_list:
    print(stu)

name = input('name:')
age = input('age:')
# f引用变量内容
info = f'''
------------ info of {name} -----------
Name : {name}
Age : {age}
'''
print(info)

#成绩判断习题
cript = float(input('请输入你的成绩：'))
if 90 < cript <100:
    print("你的成绩为A")
elif 80 <= cript <=89:
    print("你的成绩为B")
elif 60<= cript <=79:
    print("你的成绩为C")
elif 40<= cript <=59:
    print("你的成绩为D")
elif 0<= cript <=39:
    print("你的成绩为E")

