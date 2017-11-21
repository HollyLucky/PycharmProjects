# # #我是注释
# # a=100
# # if a>=0:
# #     print(a)
# # else:
# #     print(-a);
# # print(r'\\\t\\')
# # print('\\\t\\')
# # print('''line1
# # line2
# # line3''')
# # print(3>2)
# # a=123#a是一个整型数据
# # print(a)
# # a='hah'#a是一个字符串
# # print(a)
# # a='abc'
# # b=a
# # a='xyz'
# # print(b)
# # print(10/3)
# # print(10//3)
# # print(10/1)
# # b=ord('侯')
# # print(b)
# # c=chr(20399)
# # print(c)
# # print('\u4e2d\u6587')
# # print('ABC'.encode('ascii'))
# # print('侯运生'.encode('utf-8'))
# # print('ABC'.encode('utf-8'))
# # print(b'\xe4\xbe\xaf\xe8\xbf\x90\xe7\x94\x9f'.decode('utf-8'))
# # print(b'ABC'.__len__())
# # print('侯運生'.__len__())
# # print('侯运生'.encode('utf-8').__len__())
# # print('Hello %s 欢迎来到我的世界'%'侯运生')
# print('你好！%s客户，您当前的话费%d'%('侯運生',56))
# # print('您当前的股份为%d%%'%10)
# # classmates=['Machael','Bob','Tracy']
# # print(classmates)
# # a=len(classmates)
# # print(a)
# # list=["a","b","c"]
# # print(list[-1])
# # classmates.append('Adam')
# # print(classmates)
# # classmates.insert(1,'Jack')
# # print(classmates)
# # print(classmates.pop())
# # print(classmates)
# # classmates.pop(1)
# # print(classmates)
# # classmates=('Macheal','Bob','Tracy')
# # print(classmates[0])
# # t=('a','b',['A','B'])
# # t[2][0]='x'
# # t[2][1]='y'
# # print(t)
# # age=int(input('输入你的年龄：'))
# # if  age >= 18:
# #     print('你已经成年了')
# # elif age >= 15:
# #     print('你已经青年了')
# # else:
# #     print('你还是个孩子')
# # if  age>=6:
# #     print('1')
# # elif age>=10:
# #     print('2')
# # else:
# #     print(3)
# # if 2:
# #     print(1)
# # xasd='AVC'
# # if xasd:
# #     print(2)
# # names=['Micheal','Bob','Tracy']
# # for name in names:
# #     print(name)
# # sum=0
# # for x in list(range(101)):
# #     sum+=x
# # print(sum)
# # i=99
# # sum=0
# # while i>0:
# #     sum+=i
# #     i-=2
# # print(sum)
# # n=1
# # while n<=100:
# #     if n>10:
# #         print(n)
# #         break
# #     n+=1
# # print('END')
# #d={'Michael':95,'Bob':90,'Tracy':58}
# # print(d['Michael'])
# # d['HYS']=100
# # print(d)
# # d['HYS']=200
# # print(d)
# # print('WJY' in d)
# # print(d.get('Thomas',-1))
# # s=set([1,1,2,2,3,3])
# # print(s)
# # s.add(4)
# # print(s)
# # s.add(4)
# # print(s)
# # s.remove(4)
# # print(s)
# # s1=set([1,2,3])
# # s2=set([2,3,4])
# # print(s1 & s2)
# # print(s1|s2)
# # l=['a','b','c']
# # l.reverse()
# # print(l)
# # l={(1,2,3),1,4}
# # print(l)
# # l={([1,2],3,4),5,6}
# # print(l)
# # l1=[1,2,3,4,5]
# # i1=l1.__iter__()
# # print(any(i1))
# # print(i1.__next__())
# # print(i1.__next__())
# # print(i1.__next__())
# # i2=iter(l1)
# # print(any(i2))
# # print(i2.__next__())
# # print(i2.__next__())
# # print(i2.__next__())
# # print(i2.__next__())
# # x=abs(10.2)
# # print(x)
# # a=hex
# # print(a(255))
# # def my_abs(x):
# #     if x>=0:
# #         return x
# #     else:
# #         return -x
# # print(my_abs(-100))
# # def nop():
# #     pass
# # age=int(input('输入你的年龄：'))
# # if age>=18:
# #     pass
# # def my_abs(x):
# #     if not isinstance(x,(int,float)):
# #         raise TypeError('输入参数类型不正确')
# #     if x>=0:
# #         return x
# #     else:
# #         return -x
# # my_abs('sea')
# # import math
# # def move(x,y,step,angle=0):
# #     nx=x+step*math.cos(angle)
# #     ny=y+step*math.sin(angle)
# #     return  nx,ny
# # x,y=move(100,100,60,math.pi/6)
# # print(x,y)
# # import math
# # a=int(input('a='))
# # b=int(input('b='))
# # c=int(input('c='))
# # def quaduatic(a,b,c):
# #     if (not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float))):
# #         raise TypeError('输入的数据类型不对')
# #     z=b*b-4*a*c
# #     if z<0:
# #         print('该方程没解！')
# #     elif z==0:
# #         print('该方程只有一个解:%2f'%(-b/(2*a), ))
# #     else:
# #         print('该方程有两个解:%2f,%2f'%(float((-b+math.sqrt(z))/(2*a)),float((-b-math.sqrt(z))/(2*a))))
# #         return
# # quaduatic(a,b,c)
# # def enroll(name,gender,age=6,city='Beijing'):
# #     print('name:',name)
# #     print('gender:',gender)
# #     print('age:',age)
# #     print('city:',city)
# # enroll('Bob','M')
# # enroll('Lily','WM',9)
# # def add_end(L=[]):
# #     L.append('END')
# #     return L
# # print(add_end())
# # print(add_end())
# # def add_end(L=None):
# #     if L is None:
# #         L=[]
# #     L.append('END')
# #     return L
# # print(add_end())
# # print(add_end())
# # print(add_end(['1','2']))
# # def calc(numbers):
# #      sum=0
# #      for n in numbers:
# #          sum+=n*n
# #      return sum
# # print(calc([]))
# # def calc(*numbers):
# #     sum=0
# #     for n in numbers:
# #         sum+=n*n
# #     return sum
# # print(calc(1,2,3,4))
# # def person(name,age,**kw):
# #     print('name:%s,age:%s'%(name,age))
# #     print(kw)
# # person('HYS',22,city='Beijing',gender='M')
# # def person(name,age,**kw):
# #     if 'city' in kw:
# #         pass
# #     if 'job' in kw:
# #         pass
# #     person('name:',name)
# # def person(name,age,**kw):
# #     if 'city' in kw:
# #         pass
# #     if 'job' in kw:
# #         pass
# #     print('name:',name,'age',age,'other',kw)
# #     person('Jack',20,city='Beijng',addr='Cahoyang')
# # def person(name,age,*,city,job):
# #    print(name,age,city,job)
# # person('HYS',20,city='SY',job='Engineer')
# #递归函数
# # def fact(n):
# #     if(n==1):
# #         return 1
# #     return fact(n-1)*n
# # print(fact(5))
# # print(fact(100))
# # # print(fact(1000))栈溢出
# # def fact(n):
# #     return fact_inter(n,1)
# # def fact_inter(num,product):
# #     if num==1:
# #         return product
# #     return fact_inter(num-1,num*product)
# # print(fact(10))
# # def move(n,a,b,c):
# #     if n==1:
# #         print('%s->%s'%('a','b'))
# #     else:
# #         move(n-1,a,c,b)
# #         move(1,a,b,c)
# #         move(n-1,b,a,c)
# # move(3,'a','b','c')
# # L=[]
# # def add_L(n):
# #     while n>0:
# #         L.append(n)
# #         n-=2
# #     return L
# # print(add_L(99))
# # L=['Macheal','Tracy','Bob','Jack']
# # print(L[1:2])
# # L=list(range(100))
# # print(L[:10:2])
# # print((0,1,2,3,4,5,6)[:3])
# # from itertools import count
# # counter=count(start=13)
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # d={'a':1,'b':2,'c':3,'d':4}
# # for key in d:
# #     print(key)
# # for value in d.values():
# #     print(value)
# # for k,v in d.items():
# #     print(k,v)
# # from collections import Iterable
# # print(isinstance('abc',Iterable))
# # print(isinstance([1,2,3],Iterable))
# # print(isinstance((1,),Iterable))
# # for i,value in enumerate(['A','B','C']):
# #     print(i,value)
# # print(list(range(1,11)))
# # L=[]
# # for x in range(1,11):
# #     L.append(x*x)
# # print(L)
# print([x*x for x in range(1,11)])
# print([m+n for m in 'ABC' for n in 'XYZ'])
# # import os
# # print([d for d in os.listdir('.')])
# # L=['Hys','Fcj',18,'Hyc',None]
# # print([s.lower() for s in L if s and isinstance(s,str)])
# # g=(x*x for x in range(1,11))
# # print(ord('A'))
# # print(chr(65))
# # g=(x*x for x in range(10))
# # for n in g:
# #     print(n)
# # def fib(max):
# #     n,a,b=0,0,1
# #     while n<max:
# #         print(b)
# #         a,b=b,a+b
# #         n+=1
# #     return
# # fib(10)
# # def fib(max):
# #     n,a,b=0,0,1
# #     while n<max:
# #         yield b
# #         a,b=b,a+b
# #         n+=1
# #     return
# # f=fib(6)
# # print(f)
# # for x in f:
# #     print(x)
# # def odd():
# #     print('step1')
# #     yield (1)
# #     print('step2')
# #     yield (3)
# #     print('step3')
# #     yield (5)
# # o=odd()
# # print(next(o))
# # print(next(o))
# # def triangles():
# #     T=[1]
# #     while True:
# #         yield T
# #         T=[(T+[0])[i]+([0]+T)[i] for i in range(len(T+[0]))]
# # n = 0
# # for t in triangles():
# #     print(t)
# #     n = n + 1
# #     if n == 10:
# #         break
# # from collections import Iterable
# # print(isinstance((x for x in range(10)),Iterable))
# # from collections import Iterator
# # print(isinstance((x for x in range(10)),Iterator))
# # print(isinstance('ABC',Iterator))
# # print(isinstance(iter('ABC'),Iterator))
# # print(isinstance(iter([]),Iterator))
# # def add(x,y,f):
# #     return f(x)+f(y)
# # print(add(1,2,abs))
# # L=set([1,2,3,4,23,45356,231])
# # print(L)
# # L=set('avdsgaghsdaf')
# # print(L)
# import math
# # def f(x):
# #     return pow(x,2)
# # L=map(f,[1,2,3,4,5,6,7,8])
# # print(list(L))
# # print(list(map(str,[1,2,3,4,5,6,7,8])))
# # from functools import reduce
# # def add(x,y):
# #     return x+y
# # print(reduce(add,[1,2,3,4,5,6]))
# # from functools import reduce
# # def fn(x,y):
# #     return 10*x+y
# # print(reduce(fn,[1,2,3,4,5]))
# # from functools import reduce
# # def char2nums(s):
# #     return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# # print(list(map(char2nums,'457223')))
# # def fn(x,y):
# #     return 10*x+y
# # print(reduce(fn,map(char2nums,'1231676')))
# # from functools import reduce
# # str=' '
# # print(str.join(['I','am','not','a','boy']))
# # def normalize(name):
# #     return name.capitalize()
# # L=['adam','hYs','fCJ','HYC']
# # print(list(map(normalize,L)))
# # from functools import reduce
# # def prod(L):
# #     def mul(x,y):
# #         return x*y
# #     return reduce(mul,L)
# # s=[3,5,7,9]
# # print('3*5*7*9=',prod(s))
# # def is_odd(n):
# #     return n%2==1
# # print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
# # def not_empty(s):
# #     return s and s.strip()
# # print(list(filter(not_empty,['A',' ','B',None,'C'])))
# # g=lambda x:x+1
# # print(g(1))
# # print(g(2))
# # from functools import reduce
# # foo=[2,18,9,22,17,24,8,12,27]
# # print(list(filter(lambda x:x%3==0,foo)))
# # print(list(map(lambda x:x*2+10,foo)))
# # print(reduce(lambda x,y:x+y,foo))
# # def odd_iter():
# #     n=1
# #     while True:
# #         n+=2
# #         yield n
# # def _not_diviable(n):
# #     return lambda x:x%n>0
# # def primes():
# #     yield 2
# #     it=odd_iter()
# #     while True:
# #         n=next(it)
# #         yield n
# #         it=filter(_not_diviable(n),it)
# # for n in primes():
# #     if n<1000:
# #         print(n)
# #     else:
# #         break
# #
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
# L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# print(L[0][0])
# print(by_name(L))
# L2=sorted(L,key=by_name)
# L3=sorted(L,key=by_score)
# print(L2)
# print(L3)
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1())
# print(f1)
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():'% func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print('2015-5-25')
# now()
# print(int('12345',base=8))
# import functools
# int2=functools.partial(int,base=2)
# print(int2('1000000'))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
