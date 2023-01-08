# AUTHOR    ：Lv Wenchao
# coding    : utf-8
# @Time     : 2022/8/10 17:38
# @FileName : socket_http.py
# @Software : PyCharm
# request->urlib->socket
import socket
from urllib.parse import urlparse


def get_url(url):
    # 对url进行解析
    # urlparse("scheme://netloc/path;parameters?query#fragment")
    # ParseResult(scheme='scheme', netloc='netloc', path='/path;parameters', params='',
    #             query='query', fragment='fragment')
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send("Get {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
