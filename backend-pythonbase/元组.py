#元组(tuple)可看作特殊的列表，但元组一旦建立就不能改变（修改、增加、删除）
#但可通过元组->列表->元组来间接修改元组内容

# 创建空元组
tuple_a=()
tuple_b=tuple() # 两者没区别
print(f'a的值为：{tuple_a},数据类型为：{type(tuple_a)}')
print(f'b的值为：{tuple_b},数据类型为：{type(tuple_b)}')

# 只有一个元素的元组
tuple_c=(1) #tuple_c为整型而非元组
tuple_d=(1,) #与列表不同，若只有一个元素，元素后须有","，否则被视为一个数值
print(f'a的值为：{tuple_c},数据类型为：{type(tuple_c)}')
print(f'b的值为：{tuple_d},数据类型为：{type(tuple_d)}')

# 访问元组元素
tuple_e=(1,2,3,4,5)
print(tuple_e)
print(tuple_e[0])
print(tuple_e[-1])

# 访问多元素
print(tuple_e[1:3]) # a:b为左闭右开区间

# len()
print(len(tuple_e))

# 修改元组元素
tuple_e=list(tuple_e)
print(type(tuple_e))
tuple_e[1]=0
tuple_e=tuple(tuple_e)
print(tuple_e,type(tuple_e))

# 元组操作函数
tuple_f=(2,4,5,87,2,3)

# count()
print(tuple_f.count(2))

# index()
print(tuple_f.index(5))