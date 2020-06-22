#encoding: utf-8

line = "I am super man!"

#string的split方法
print(line.split("[ m]"))

#re的split方法
import re
print(re.split("[ m]", line))