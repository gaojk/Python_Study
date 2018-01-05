# Author:Jing Lv
# 迭代
from collections import Iterable

# 定义一个字典
d = {"May": 18, "Jack": 20, "Jean": 16, "Abby": 25}

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 迭代key,默认情况下，dict迭代的是key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 同时迭代key和value
for key, value in d.items():
    print("%s : %s" % (key, value))

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
print(isinstance('abc', Iterable))  # str是否可迭代  True
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代 True
print(isinstance(123, Iterable))  # 整数是否可迭代 False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
l = ['a', 'b', 'c', 'd', 'e']
for i, value in enumerate(l):
    print(i, value)

# for循环里，同时引用了两个变量
lt = [(4, 2), (6, 3), (2, 1)]
for x, y in lt:
    print(x, y)
