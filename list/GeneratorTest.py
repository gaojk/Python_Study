# Author:Jing Lv
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# yield关键字

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x for x in range(1, 11)]
print(L)
print(type(L))  # <class 'list'>

G = (x for x in range(1, 11))
print(type(G))  # <class 'generator'>

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
print(next(G))  # 1
print(next(G))  # 2
print(next(G))  # 3
print(next(G))  # 4

print('--------------------------------------------')

# 创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in G:
    print(n)

print('--------------------------------------------')


# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


'''
赋值语句：
a, b = b, a + b
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''
print(fib(6))

print('--------------------------------------------')

'''
fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
'''


def fib_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
print(fib_yield(6))  # <generator object fib_yield at 0x000002626867B3B8>


# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3


# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
print(next(o))
# step1
# 1
print(next(o))
# step2
# 2
print(next(o))
# step3
# 3
# print(next(o))  # 抛出异常StopIteration
'''
可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
'''
print('--------------------------------------------')
# 使用for循环来迭代fib_yield
for i in fib_yield(6):
    print(i)

print('--------------------------------------------')
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib_yield(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 将杨辉三角的每一行看成一个list,写一个生成器（generator）,不断输出下一行list
def triangel(n):
    L = [1]  # 定义一个list[1]
    while True:
        yield L  # 打印出该list
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]  # 计算下一行中间的值（除去两边的1）
        L.insert(0, 1)  # 在开头插入1
        L.append(1)  # 在结尾添加1
        if len(L) > 10:  # 仅输出10行
            break

print('--------------------------------------------')
# 生成一个generator对象，然后通过for循环迭代输出每一行
a = triangel(10)
for i in a:
    print(i)

'''
注：普通函数和generator生成器的区别：
1.普通函数调用直接返回结果，generator函数的调用，返回一个generator对象；（调用generator时可以先创建一个对象，再用next()方法不断获得下一个返回值，但实际中通常用for循环实现）
2.generator在执行过程中，遇到yield就中断，下次又继续执行
'''
