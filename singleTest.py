"""

"""
from socket import *
import os


# HOST = '176.23.6.'
HOST = 'localhost'
PORT = 8888
ADDR = (HOST, PORT)

client_socketfd = socket()
# client_socketfd.bind(("176.23.6.118", 12308))
client_socketfd.connect(ADDR)

send_msg = '你好!我是练习时长两年半的个人练习生蔡徐坤,喜欢唱、跳、Rap、篮球,music!\n' \
           '图片.jpg'.encode()
client_socketfd.send(send_msg)
recv_msg = client_socketfd.recv(1024).decode()
print("From server:" + recv_msg)
client_socketfd.close()























