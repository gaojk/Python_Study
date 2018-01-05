# Author:Jing Lv
# 列表生成式
import os

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1, 11)))

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法一：
L = []
for i in range(1, 11):
    L.append(i * i)
print(L)

# 方法二：
print([i * i for i in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([i * i for i in range(1, 11) if i % 2 == 0])

# 还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABCDEFG' for n in "HIJKLMN"])

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现:
print([d for d in os.listdir()])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {"May": 18, "Jack": 20, "Jean": 16, "Abby": 25}
for key, value in d.items():
    print(key, "=", value)

print([key + "=" + str(value) for key, value in d.items()])

# 把一个list中所有的字符串变成小写
l = ["HELLO", "WORLD", "APPLE", "WA"]
print([s.lower() for s in l])