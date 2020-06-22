#encoding: utf-8

# 导入 socket 模块
import socket

# 创建 socket 对象
s = socket.socket()

#连接服务端
s.connect(("127.0.0.1", 6666))
print s.recv(1024)
s.close()