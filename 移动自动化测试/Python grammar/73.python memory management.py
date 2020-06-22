#encoding: utf-8
from sys import getrefcount

#引用计数
a1 = 10000000
a2 = 10000000
#del a1
del a2

print(id(a1))
#print(id(a2))

#检验a1和a2是同一个东西
#print(a1 is a2)

# #获取a2的引用计数
print(getrefcount(a1))
