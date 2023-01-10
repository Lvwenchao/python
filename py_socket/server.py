# AUTHOR    ：Lv Wenchao
# coding    : utf-8
# @Time     : 2022/8/10 16:57
# @FileName : server.py
# @Software : PyCharm
import socket

# ipv4协议和Socket类型
# 流式Socket（STREAM）：是一种面向连接的Socket，针对于面向连接的TCP服务应用，安全，但是效率低；
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址和端口
server.bind(('0.0.0.0', 8000))
# 监听
server.listen()
# 接受（阻塞）获取连接对象和地址
sock, addr = server.accept()
print("连接地址", addr)

# 获取从客户端发送的数据
# 一次获取1k的数据
data = sock.recv(1024).decode('utf-8')
sock.send("Hi,{}".format(data.split()[-1]).encode())
sock.close()
server.close()
