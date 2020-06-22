#encoding: utf-8
import re

s1 = "helloworld, helloworld"
w1 = 'hello'
w2 = 'world'

#search扫描整个字符串
print(re.search(w2, s1))
print(re.search(w2, s1).group())

#match只在字符串开始的位置匹配
print(re.match(w2, s1))
print(re.match(w2, s1).group())