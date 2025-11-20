# 空列表
list_a=[]
list_b=list() #两者没有区别
print(f'a的值为：{list_a},数据类型为：{type(list_a)}')
print(f'b的值为：{list_b},数据类型为：{type(list_b)}')

# 只有一个元素的列表
list_c=[1]
print(list_c)

# 有多元素的列表(元素可以是任意数据类型)
list_d=[1,'a',110.5,[1,2,3]]
print(list_d)

# 二维列表
list_e=[[1,2],[3,4],[5,6],]
print(list_e)

# 访问列表元素(从0开始，-1为最后一个元素)
print(list_d[0],list_d[3],list_d[0:4]) # a:b为左闭右开
# len()获取列表长度
print(f'list_d的长度为：{len(list_d)}')

# 列表运算
# 加法+(相当于拼接,类似strcat)
list_f=list_c+list_d
print(list_f)
# 乘法*(相当于连续+)
list_g=list_c*3
print(list_g)

# 列表操作函数（方法）
list_h=[1,2,3,4,5]
print(list_h)

# list.append(x)                列表尾部追加元素 x
list_h.append(1)
print(list_h)

# list.count(x)                 返回列表中的参数x出现的次数
print(list_h.count(1))

# list.extend(L)                向列表中追加另一个列表 L
list_h.extend([6,7,8])
print(list_h)

# list.index(x)                 返回参数 x 在列表中的序号（x 不存在则报错）
print(list_h.index(2))

# list.insert(index, object)    向列表中指定位置(index)插入元素（object）
list_h.insert(3,0)
print(list_h)

# list.pop()                    删除列表中尾部的元素并返回删除的元素
print(list_h.pop())
print(list_h)

# list.remove(x)                删除列表中的指定元素（有多个则只删除第一个），指定元素不存在则报错
list_h.remove(1)
print(list_h)

# list.reverse()                将列表中元素的顺序颠倒
list_h.reverse()
print(list_h)

# list.sort()                   将列表中元素排序（要求其成员可排序，否则报错）
list_h.sort()
print(list_h)