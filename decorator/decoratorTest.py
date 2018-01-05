# Author:Jing Lv
from datetime import datetime
import functools

"""
装饰器
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
装饰器其实也就是一个函数，一个用来包装函数的函数，装饰器在函数申明完成的时候被调用，
调用之后申明的函数被换成一个被装饰器装饰过后的函数
"""


# 无参装饰器
# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print("Hello, %s():" % func.__name__)  # 函数对象有一个__name__属性，可以拿到函数的名字
        return func(*args, **kw)

    return wrapper


# log是一个decorator，接受一个函数作为参数，并返回一个函数。借助Python的@语法，把decorator置于函数的定义处
@log
def now():
    print(datetime.now())


# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now()  # 把@log放到now()函数的定义处，相当于执行了语句:now = log(now)
"""
1.log()是一个decorator，返回一个函数,原来的now()函数仍然存在
2.现在同名的now变量指向了新的函数,于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
3.wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
4.在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
"""
print(now.__name__)  # 运行结果：wrapper
print('-----------------------------------------------------------------------------------------')


# 带参装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("Hello, %s, %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log("action")
def now1():
    print(datetime.now())


now1()  # 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数
print(now1.__name__)  # 运行结果：wrapper
print('-----------------------------------------------------------------------------------------')

print('-----------------------------------------------------------------------------------------')


# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("Hello, %s():" % func.__name__)  # 函数对象有一个__name__属性，可以拿到函数的名字
        return func(*args, **kw)

    return wrapper


@log3
def now3():
    print(datetime.now())


now3()
print(now3.__name__)
print('-----------------------------------------------------------------------------------------')


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("Hello, %s, %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log("WaO")
def now4():
    print(datetime.now())


now4()
print(now4.__name__)
