# Author:Jing Lv

"""
匿名函数,无函数名
关键字lambda表示匿名函数
lambda(关键字) x(函数参数)
lambda x: x*x
等价于
def f(x):
    return x*x
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
也可以把匿名函数作为返回值返回
"""
f1 = lambda n: n * 2
f2 = lambda x, y: x ** y

print(f1(5))  # 执行结果10
print(f2(2, 2))  # 执行结果4


def f3(x, y):
    return lambda: x * y

a = f3(5, 7)
print(a)
