# std1={'name':'Machael','score':98}
# def print_score(st):
#     print(st['name'],st['score'])
# print_score(std1)
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print(self.name,self.score)
# bart=Student('Bart',59)
# hys=Student('Lisa',98)
# bart.print_score()
# hys.print_score()
# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def print_stu(self):
#         print(self.__name,self.__score)
#     def get__name(self):
#         return self.__name
#     def get__score(self):
#         return self.__score
#     def set_score(self,score):
#         if 0<=score<=100:
#             self.__score = score
#         else:
#             raise ValueError('不在范围内')
# bat=Student('Bart',95)
# bat.set_score(96)
# print(bat.get__name(),bat.get__score())
# print(type(123))
# print(type([1,2,3]))
# print(type(None))
# print(type(123)==type(345))
# print(type(123)==int)
# print(type(abs))
# import types
# def fn():
#     pass
# print(type(fn)==types.FunctionType)
# print(type((x for x in range(10)))==types.GeneratorType)
# print(type(abs)==types.BuiltinFunctionType)
# print(isinstance([1,2,3],(list,tuple)))
# print(dir('ABC'))
# class MyObject(object):
#     name='Student'
#     def __init__(self):
#         self.x=9
#     def power(self):
#         return self.x*self.x
# obj=MyObject()
# print(hasattr(obj,'x'))
# print(hasattr(obj,'y'))
# print(obj.x)
# print(setattr(obj,'y',19))
# print(getattr(obj,'y'))
# print(getattr(obj,'z',404))
# st=MyObject()
# st.name='Bob'
# st.score=99
# print(MyObject.name)
# print(st.name)
# del st.name
# print(st.name)
# class Student(object):
#     pass
# def set_age(self,age):
#     self.age=age
#     return self.age
# s=Student()
# from types import MethodType
# s.set_age=MethodType(set_age,s)
#
# print(s.set_age(25))
# s1=Student()
# # print(s1.set_age(23))
# class Student(object):
#     __slots__ = ('name','age')
#     pass
# s=Student()
# s.name='HYS'
# s.age=19
# # s.score=20
# class GraduateStudent(Student):
#     pass
# ss=GraduateStudent()
# ss.score=99
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('输入的应该是整数')
#         if 0<=value<=100:
#             self._score=value
#         else:
#             raise ValueError('输入的分数越界了')
#     @property
#     def birth(self):
#         return self.birth
#     @birth.setter
#     def birth(self,birth):
#         self._birth=birth
#     @property
#     def age(self):
#         return 2017-self._birth
# s=Student()
# s.score=60
# print(s.score)
# s.birth=1995
# print(s.age)
# class Student():
#     def __init__(self,name):
#         self.name=name
#     def __len__(self):
#         print(1)
#     def __str__(self):
#         return 'Student object(name:%s)'% self.name
#     __repr__=__str__
# print(Student('HYS'))
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=1,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
#     def __getitem__(self, n):
#         if isinstance(n,int):
#             for x in range(n):
#                 self.a,self.b=self.b,self.a+self.b
#             return  self.a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(self.a)
#                 self.a,self.b=self.b,self.a+self.b
#             return L
#
#
#
# for n in Fib():
#     print(n)
# f=Fib()
# print(f[0:5])
# # from enum import Enum
# # Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec'))
# # for name,member in Month.__members__.items():
# #     print(name,'->',member,',',member.value)
# from enum import Enum
# Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# for name,member in Month.__members__.items():
#     print(name,'->',member,',',member.value)
# from enum import Enum ,unique
#
# @unique
# class Weekday(Enum):
#     Sun=1
#     Mon=2
#     Tue=3
#     Wed=4
#     Thu=5
#     Fri=6
#     Sat=7
# for name,member in Weekday.__members__.items():
#     print(name,'->',member,'->',member.value)
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
# from hello import Hello
# h=Hello()
# print(type(h))
# print(type(Hello))
# def fn(self,name='world'):
#     print('Hello,%s'%name)
# Hello=type('Hello',(object,),dict(hello=fn))
# h=Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))
# class ListMetaclass(type):
#     def __new__(cls, name,bases, attrs):
#         attrs['add']=lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)
# class MyList (list,metaclass=ListMetaclass):
#     pass
# L=MyList()
# L.add(1)
# print(L)
# L2=list()
# L2.append(1)
# print(L2)
# try:
#     print('try...')
#     r=10/2
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except',e)
# finally:
#     print('finally...')
# print('END')
# try:
#     print('')
# print(int('18',base=16))
# print(int('18',16))
# try:
#     print('try...')
#     r=10/int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError',e)
# except ZeroDivisionError as e:
#     print('ZeroDiv：',e)
# else:
#     print('no Error')
# finally:
#     print('finally..')
# print('END')
# def fn():
#     a=10/int('a')
#     print('result:',a)
#     return a
# try:
#     fn()
# except BaseException as e:
#     print('BaseException:',e)
# except ValueError as e:
#     print('ValueError:',e)
# except UnicodeError as e:
#     print('UnicodeError:',e)
# else:
#     print('no error!')
# finally:
#     print('final...')
# print('END')
# import logging
# def fs(s):
#     a=10/int(s)
#     return a
# def bar(s):
#     a=fs(s)*2
#     return a
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')
# class FooError(ValueError):
#     pass
# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value:%s'%s)
#     return 10/n
# foo('0')
# def fn(s):
#     n=int(s)
#     assert n!=0,'n is zero!'
#     return 10/n
# def main():
#     fn('-0')
# main()
# import logging
# logging.basicConfig(level=logging.DEBUG)
# s='0'
# n=int(s)
# logging.debug('n=%d'%n)
# print(10/n)
import pdb
s='0'
n=int(s)
print(10/n)
