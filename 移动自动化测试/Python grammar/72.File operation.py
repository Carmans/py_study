#encoding: utf-8

#写文件
f = open('test.txt', 'wt')
f.write("hello world")
f.close()

#使用with，追加内容，不用关系文件关闭问题
with open("test.txt", 'at') as f:
    f.write("\nhello mook")

#读取文件
with open("test.txt", 'rt') as f:
    print(f.read())