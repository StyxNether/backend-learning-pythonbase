#字典(dict),用大括号{}包围，以键值对形式声明和存在，内部无序，只能通过键访问成员
#有点像Lua的表(table)?

# 创建空字典
dict_a={}
dict_b=dict()
print(f'a:{dict_a}，数据类型:P{type(dict_a)}')
print(f'a:{dict_b}，数据类型:P{type(dict_b)}')

# 多元素字典
dict_c={
    'a':1,
    'b':2,
    2:'c',
    3:[1,2,4],
    3.3:(1,2,'d'),
    }
print(dict_c)

# 查询字典值
print(dict_c['a'])

# 通过键名修改值
dict_c[2]=0
dict_c['a']=5
print(dict_c)

# 字典操作函数（方法）
dict_e={'a':1,'b':2,'c':3,'d':4}
# dict.items() – 获得由键和值组成的迭代器
# dict.keys() – 获得键的迭代器
# dict.values() – 获得值的迭代器
# dict.fromkeys(iter, value) – 以列表或元组中给定的键建立字典，默认值为 value
# dict.popitem() – 从字典中删除任一键值对并返回它
# dict.setdefault(k, default) – 若字典中存在键 k，则返回其对应的值；否则，在字典中建立一个 k: default 字典成员

# dict.get(key, [default]) – 获得键 key 对应的值，不存在则返回 default
print(dict_e.get('e','不存在'))

# dict.pop(k) – 删除 k:v 键值对
dict_e.pop('a')
print(dict_e)

# del关键字
del dict_e['b']
print(dict_e)

# dict.update(dict_1) – 从另一个字典更新成员，不存在则创建，存在则覆盖(批量更新)
# 也可用dict[a]=b来单个更新
dict_e.update({'b':3})
print(dict_e)

# 不能用=来给字典赋值，=对字典而言是引用（浅拷贝）
dict_f=dict_e
print(f'f:{dict_f}, e:{dict_e}')
dict_f['a']=0
print(f'f:{dict_f}, e:{dict_e}')

# dict.copy() – 复制字典（深拷贝）
dict_g=dict_e.copy()
print(f'g:{dict_g}, e:{dict_e}')
dict_g['a']=2
print(f'g:{dict_g}, e:{dict_e}')

# dict.clear() – 清空字典
dict_e.clear()
print(dict_e)