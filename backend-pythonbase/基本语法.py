# 单行注释
'''多行
注释'''
"""多行
注释"""

# print("你好，VS Code！")

# 变量
a = 10
b = 20
# 一行中为多个变量赋值
x, y, z = 1, 2, 3

# 输出 print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# value -- 要输出的值，可以是多个，用逗号隔开
# sep -- 用于分隔多个值，默认是一个空格
# end -- 用于结尾，默认是换行符
# file -- 要写入的文件对象，默认是sys.stdout，即控制台
# flush -- 是否强制刷新输出缓冲区，默认是False
# 转义字符\,可用R/r'内容'或R/r"内容"表示原始字符串，不进行转义
print(R"Hello,\nWorld!")
print(a, b, sep=' + ', end=' = ')
print(x, y, z, sep=', ')

# 输入 input(prompt=None)
# prompt -- 提示信息，显示在输入前面
# ！！！ input函数接收的所有输入内容都作为字符串处理！！！使用时注意类型转换
temp = int(input("请输入一个数字："))
print("你输入的数字是：", temp)
name = input("请输入你的名字：")
# 输出时，不同输出值以逗号作为分隔符，sep属性只应用在不同输出值之间，而不用于输出值内部各部分
# 同一输出值内，各部分用+连接
print("你好，" + name + "！" + name, name, sep='&')

# 数据类型 可用type(变量)函数获取数据类型
# 整型 int
num1 = 100
# 浮点型 float
num2 = 3.14
# 字符串 str 单引号('') 双引号("") 三单引号(''' ''') 三双引号(""" """)
# 三引号可以表示多行字符串
str1 = "Hello, World!"
print("""
这是一个多行
      字符串。
      前后自动换1行(独立于end属性)。
""",end=" end ")
# 布尔型 bool
flag = True
# 复数 complex
complex_num = 3 + 4j

# 算数运算符
# ** 幂运算符, *乘法, /除法, //取整除, %取模, +加法, -减法

# 字符串运算
str2 = "Hello"
str3 = "Python"
str4 = str2 + " " + str3  # 字符串连接
print(str4)
str5 = str3 * 3  # 字符串重复
print(str5)
str6 = "Hello, World!"
print(str6[7:12])  # 字符串切片，输出World