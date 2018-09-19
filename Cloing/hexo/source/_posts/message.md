---
title: message
date: 2018-09-10 19:13:20
tags:
---
- 多态
```
对象的多种形态
比如说动物，动物分为很多种但是动物都会吃东西，但是动物吃的东西又不一样
#  有三种动物：狗、猫、猪，
#	父类：动物、
#	子类：狗、猫、猪   可以添加子类自己的方法，自己扩展
#	动物的属性：动物的名字
#	动物的方法是eat（就是打印自己的名字）
#   有一个饲养员：饲养员
#	饲养员的方法：feed_animal(需要饲养的动物)
#		函数的实现是（其实就是调用动物的eat方法）
class Animal(object):
    name="动物"
    def eat(self):
        print("%s会吃东西"%(self.name))
class Dog(Animal):
    def eat(self):
        print("小狗吃骨头")

class Cat(Animal):
    def eat(self):
        print("小猫爱吃鱼")

class Pig(Animal):
    def eat(self):
        print("小猪不知道吃什么")


class Breeder(object):
    def feed_animal(self,animal):
        animal.eat()        

breeder=Breeder()
dog=Dog()
breeder.feed_animal(dog)
cat=Cat()
breeder.feed_animal(cat)
pig=Pig()
breeder.feed_animal(pig)
```
- 手写单例模式
举个常见的单例模式例子，我们日常使用的电脑上都有一个回收站，在整个操作系统中，回收站只能有一个实例，整个系统都使用这个唯一的实例，而且回收站自行提供自己的实例。因此回收站是单例模式的应用。
单例模式，是一种常用的软件设计模式。在它的核心结构中
只包含一个被称为单例的特殊类。
通过单例模式可以保证系统中，应用该模式的类一个类只有一个实例。即一个类只有一个对象实例。
```
class A(object):
    # 定义类属性记录实例化对象
    __instance = None
    
    # 创建实例对象的方法
    def __new__(cls):
        # 如果没有创建实例对象就创建
        if cls.__instance == None: 
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #如果存在就直接返回
            return cls.__instance
```
```
# 创建单例时，只执行1次__init__方法
 class Singleton(object):
    # 定义雷属性记录实例化对象
    __instance = None
    #创建市里的方法
    def __new__(cls):
        if cls.__instance = None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    
    def __init__(self, name):
        self.name = name

    怎么保证打印的名字是一个呢？

class Singleton(object):
    __instance = None
    # 标志语，false没有赋值 ture 已经赋值
    __init__flag = False
    重写new方法,创建对象记录下来
    下次创建对象的时候不去创建新的对象，而是返回已经创建的对象
    def __new__(cls):
    if cls.__instance = None:
        cls.__instance = object.__new__(cls)
        print('创建新对象的地址',id(cls.__instance)
        return cls.__instance
        return cls.__instance
    else:
        return cls.instance
    def __init__(self, name):
    if Singleton.__init__flag = False:
        self.name = name
        Singleton.__init__flag = True
```
- 介绍一下工厂模式
工厂模式是一个在软件开发中用来创建对象的设计模式。
工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。
当程序运行输入一个“类型”的时候，需要创建于此相应的对象。这就用到了工厂模式。在如此情形中，实现代码基于工厂模式，可以达到可扩展，可维护的代码。当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类。
简单工厂模式的实质是由一个工厂类根据传入的参数，动态决定应该创建哪一个产品类（这些产品类继承自一个父类或接口）的实例。
封装函数，动态创建商品类
- 说说有哪些mvc模式的框架
Struts、Spring、ZF/.NET
耦合性低/重用性高/生命周期成本低/部署快/可维护性高/有利软件工程化管理
- 手写装饰器,冒泡,二分,快拍,上楼梯问题
```
装饰器
def demo(name):
    print('demo--name', name)
    def demo1(demo_name):
        print('demo1--demoname', demo_name.__name__)
        def demo2():
            print('demo--name', name)
            demo_name()
        return demo2
    return demo1
@demo('zhuangshiqi')
def test():
    print('test')
test()
冒泡
def damo(sun):
    for i in range(len(sun)-1):
        for j in range(len(sun)-i-1):
            if sun[j]> sun[j+1]:
                sun[j], sun[j+1] = sun[j+1], sun[j]
    return sun
python 二分
时间复杂度为o（logN）
    def demo(array, t):
        for i in range(len(array):
            if array[i] == t:
                return True
        return False
    
    def demo1(array, t):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = int((left+right)/2)
            if array[mid] < t:
                left = mid+1
            elif array[mid] > t:
                right = mid -1
            else:
                return True
        return False
    array = list(range(100000))
    import time 
    t1 = time.time()
    demo(array,100001)
    t2 = time.time()
    print('线性查找', t2-t1)

    t3 = time.time()
    demo1(array, 100001)
    t4 = time.time()
    print('二分查找', t4-t3)
链表
1-->2-->3-->4-->5-->null
5-->4->3-->2-->1-->null
class Demo(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Demo1(object):
    def reverseList(self,head):
        dummy = head
        tmp = dummy

        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy
        return dummy

head = Demo(1)
head.next = Demo(2)
head.next.next = Demo(3)
head.next.next.next = Demo(4)
head.next.next.next.next = Demo(5)

demo1 = Demo1()
reverse_head = demo1.reverseList(head)
tmp = reverse_head

while tmp:
    print(tmp.val)
    tmp = tmp.next

python 快速排序
def demo(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1], A[r] = A[r],A[i+1]
    return  i + 1
def demo2(A,p,r):
    if p< r:
        q = demo(A,p,r)
        demo(A,p,q-1)
        demo(A,q+1,r)
A = [23,54,6,5,7,8]
# 0,4代表列表的下标
demo2(A,0,4)
Pprint(A)
python 上楼梯问题
    def demo(n):
        a = 1
        b = 2
        c = 3
        for i in range(n-3):
            c,b,a = a+b+c, c, b
        return c
其实就是斐波那契数列
def demo(n):                  
    if n == 1:                
        return 1              
    if n == 2:                
        return 2              
    a,b = 1, 2                
    result = 0                
    for i in range(3, n+1):   
        result = a + b        
        a = b                 
        b = result            
    return result             
                              
print(demo(10))               
                              
- 字典按值排序
方法1
f = zip(x.values(),x.keys())
sorted(f)
方法2
sorted(x.items(), key = lambda x:x[1], reverse = True)
- 字典key value互换
使用zip压缩器
使用字典推导式
{v: k for k ,v in x.items()}
- 来来以深度优先遍历二叉树
```
class TreeNode(object): #定义二叉树类

    def __init__(self,val,left=None,right=None):

        self.val = val

        self.left = left

        self.right = right

 

class BinaryTree(object):

    def __init__(self,root=None):

        self.root = root

 

    def preScan(self,retList, node): #先序遍历：先跟、再左、后右

        if node != None:

            retList.append(node.val)

            self.preScan(retList, node.left)

            self.preScan(retList, node.right)

        return retList

 

    def midScan(self, retList, node): #中序遍历：先左、再跟、后右

        if node != None:

            self.midScan(retList, node.left)

            retList.append(node.val)

            self.midScan(retList, node.right)

        return retList

 

    def postScan(self, retList, node): #后序遍历：先左、再右、后跟

        if node != None:

            self.postScan(retList, node.left)

            self.postScan(retList, node.right)

            retList.append(node.val)

        return retList

 

if __name__ =='__main__':

    root = TreeNode(50)

    root.left = TreeNode(20,left=TreeNode(15),right=TreeNode(30,right=TreeNode(12)))

    root.right = TreeNode(60,right=TreeNode(70))

bTree = BinaryTree(root)

retList = bTree.preScan([],bTree.root)

print retList

retList2 = bTree.midScan([],bTree.root)

print retList2

retList3 = bTree.postScan([],bTree.root)

print retList3

```
- 广度优先遍历二叉树
```

'''
二叉树结点
'''  
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def settag(self,tag=None):
        self.tag = tag
 
def visit(treenode):

    print(str(treenode.val),end=' ')
import queue
'''
广度优先遍历
'''  
def levelOrder(root):
    deque = queue.Queue()
    if(root is not None):
        deque.put(root)
    while(not deque.empty()):
        treenode = deque.get()
        visit(treenode)
        if(treenode.left is not None):
            deque.put(treenode.left)
        if(treenode.right is not None):
            deque.put(treenode.right)

```
- 说一下他们的时间复杂度和空间复杂度
一般来说，时间复杂度高的算法比复杂度低的算法慢

- 时间复杂度的最优,最差,和平均值
- 说一下线程进程协程
```
进程是系统进行资源分配和调度的一个独立单位，进程是资源分配的单位，线程是cpu调度的单位。
线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,
只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.
线程包含再进程中
```
- 协程，又程微线程，纤程，英文名：coroutine
- 而协程的操作则是程序员指定的，在python中通过yield，人为的实现并发处理。
- 协程存在的意义：
- 协程，则只使用一个线程，分解一个线程成为多个“微线程”，在一个线程中规定某个代码块的执行顺序。
- 协程的应用场景：当程序中存在大量不需要CPU的操作时（IO）。
- 首先我们得知道协程是啥？协程其实比线程更小的执行单元。 为啥说他是一个执行单元，因为他自带CPU上下文。
- 协程和线程差异：
- 线程切换非常耗性能
- 但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。
- 协程的问题-协程程序员自己调度
- 让需要执行的协程更多的获得CPU时间才是问题的关键。
- ### 计算密集型和IO密集型
- 计算密集型-->例如for循环里嵌套10层for循环-->占大量的cpu资源-->解决方案-->使用多进程不能用多线程（多线程中有个全局锁GIL）
- IO密集型->需要网络功能，大量的事件等待网络数据的到来-->多线程、协成
- 尽量不要再协程里面做IO密集型操作

- session+cookie和使用tocken有什么区别
cookie数据存放在客户的浏览器上，session数据放在服务器上。
cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗
   考虑到安全应当使用session。
   考虑到减轻服务器性能方面，应当使用COOKIE。
 将登陆信息等重要信息存放为SESSION
   其他信息如果需要保留，可以放在COOKIE中
   session 和  token并不矛盾，作为身份认证 token安全性比session好

    token就是令牌，比如你授权（登录）一个程序时，他就是个依据，判断你是否已经授权该软件；cookie就是写在客户端的一个txt文件，里面包括你登录信息之类的，这样你下次在登录某个网站，就会自动调用cookie自动登录用户名；session和cookie差不多，只是session是写在服务器端的文件，也需要在客户端写入cookie文件，但是文件里是你的浏览器编号.Session的状态是存储在服务器端，客户端只有session id；而Token的状态是存储在客户端。
- 数据库如何优化
    1.优化SQL语句
    通过添加索引进行优化
    优化Order by
         有两种方式如下：

    （1）索引优化：对by后的列添加索引，从而大达到优化的目的。

    （2）where+order by 的组合优化：通过where进行限制后在进行order by
    优化limit
    优化子查询
    2.优化数据库结构
        1、优化insert语句

            禁用索引，禁用唯一性检查，使用一条insert插入多条语句。

        2、优化update语句

            使用一个update语句同时做多个更新。

        3、优化delete语句

            删除一条记录的时间与索引的数量成正比。删除一个表的所有行，使用truncate table Tbname 而不要使用delete from table
    3.优化Mysql服务器
- Django如何优化
1利用标准数据库优化技术：索引, Django建立实体的时候，支持给字段添加索引，具体参考Django.db.models.Field.db_index。

2了解Django的QuerySets：QuerySets是有缓存的，一旦取出来，它就会在内存里呆上一段时间，尽量重用它
3数据库的工作就交给数据库本身计算，别用Python处理：使用 filter and exclude 过滤不需要的记录，这两个是最常用语句，相当是SQL的where。使用annotate对数据库做聚合运算。不要用python语言对以上类型数据过滤筛选，同样的结果，python处理复杂度要高，而且效率不高， 白白浪费内存。使用原生的SQL语句：

4如果需要就一次性取出你所需要的数据：单一动作（如：同一个页面）需要多次连接数据库时，最好一次性取出所有需要的数据，减少连接数据库次数。此类需求推荐使用QuerySet.select_related() 和 prefetch_related()。使用QuerySet.count()代替len(queryset),虽然这两个处理得出的结果是一样的，但前者性能优秀很多。同理判断记录存在时，QuerySet.exists()比if queryset实在强得太多了。

5 懂减少数据库的连接数：使用 QuerySet.update() 和 delete()，这两个函数是能批处理多条记录的，适当使用它们事半功倍；如果可以，别一条条数据去update delete处理。

使用 Redis 进行缓存
使用异步 Worker 进行写库操作
- 高并发问题
：1，悲观锁；2，乐观锁
使用场景：并发量高的时候使用悲观锁，缺点：加锁消耗资源
并发量低的时候使用乐观锁，缺点：乐观锁循环耗费时间。
- 秒杀问题,一件商品多人抢购如何处理
获取第一位的数据其他人均不满足
- 说一下事务四大特性和隔离级别
ACID
原子性（Atomicity） 要么全部完成，要么都不成功
一致性(Consistency) 几个并行执行的事务，其执行结果必须与按照某一舒徐串执行的结果相一致
隔离性(Isolation) 事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须市透明的
持久性(Durability) 对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障；
隔离级别
脏读 在一个事务处理过程里读取了另一个未提交的事务中的数据
不可重复读 在对于数据库中的某个数据，一个事务范围内多次查询却返回了不同的数据值，
虚读 是事务非独立执行时发生的一种现象
　　现在来看看MySQL数据库为我们提供的四种隔离级别：

　　① Serializable (串行化)：可避免脏读、不可重复读、幻读的发生。

　　② Repeatable read (可重复读)：可避免脏读、不可重复读的发生。

　　③ Read committed (读已提交)：可避免脏读的发生。

　　④ Read uncommitted (读未提交)：最低级别，任何情况都无法保证。
- redis的数据类型和使用场景
字符串(str)， 哈希(hash) 列表(list) 集合(set) 有序集合(zset)

- 一万件商品如何按价格排序取前十个
使用快速排序

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

A = [...]

quickSort(A, 0, 9999)
print(A[:-9])
- redis考数据类型和使用场景,比如list啥时候用,
redis 七个使用场景https://www.cnblogs.com/NiceCui/p/7794659.html
- 还有MySQL有哪些数据库引擎,有什么区别
ISAM：ISAM是一个定义明确且历经时间考验的数据表格管理方法，它在设计之时就考虑到数据库被查询的次数要远大于更新的次数
MyISAM：MyISAM是MySQL的ISAM扩展格式和缺省的数据库引擎。
InnoDB：InnoDB数据库引擎都是造就MySQL灵活性的技术的直接产品，这项技术就是MYSQL+API
MEMORY: MEMORY是MySQL中一类特殊的存储引擎。它使用存储在内存中的内容来创建表，而且数据全部放在内存中。
InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。
MyISAM：插入数据快，空间和内存使用比较低。
MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高
https://blog.csdn.net/t146lla128xx0x/article/details/78737290
- ["1","2","10"],列表里是字符型数值,如何按数字大小给列表排序
list1 = []                            
a = ["1","2","10"]                    
for i in a:                           
    b = int(i)                        
    list1.append(b)                   
print(sorted(list1, reverse=True))    
- Python2和3的区别
1. print不再是语句，而是函数
2. 在Python 3中，没有旧式类，只有新式类
 3. 原来1/2（两个整数相除）结果是0，现在是0.5了
 4. 新的字符串格式化方法format取代%
  6. xrange重命名为range
   7. !=取代 < > 
   8. long重命名为int
9. except Exception, e变成except (Exception) as e
 10. exec变成函数
- 爬虫好像问scrapy和scrapy_redis有什么区别
- 还有scrapy爬虫的执行流程,当场手写
- 看完我说的你在百度django和爬虫的面试题
- RESTfromework问得也挺多
- apiview和viewset有啥关系
- 问rest是啥