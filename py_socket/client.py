# AUTHOR    ：Lv Wenchao
# coding    : utf-8
# @Time     : 2022/8/10 16:57
# @FileName : client.py
# @Software : PyCharm
import socket

# ipv4协议和Socket类型
# 流式Socket（STREAM）：是一种面向连接的Socket，针对于面向连接的TCP服务应用，安全，但是效率低；
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主动初始化TCP服务器连接
client.connect(('127.0.0.1', 8000))
client.send("I am the client".encode('utf-8'))
data = client.recv(1024)
print(data.decode("utf-8"))
client.close()
