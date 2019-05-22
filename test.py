"""

"""
import socket
import os, sys

# 服务器地址
# host_address = ('0.0.0.0', 8889)
# host_address = ('176.23.6.118', 8888)


# 发送消息
def send_msg(client_sockfd, name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = 'quit'
        if text == 'quit':
            msg = 'Q ' + name
            client_sockfd.sendto(msg.encode(), host_address)
            sys.exit("退出聊天室")

        msg = "C %s %s" % (name, text)
        client_sockfd.sendto(msg.encode(), host_address)


# 接受消息
def recv_msg(client_sockfd):
    while True:
        data, host_address = client_sockfd.recvfrom(2048)
        # 服务端发送EXIT表示让客户端退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode())


# 创建网络连接
def main():
    client_sockfd = socket.socket(type=socket.SOCK_DGRAM)
    while True:
        # name = input('请输入姓名：')
        msg = "L " + '蔡徐坤'
        client_sockfd.sendto(msg.encode(), host_address)
        # 等待回应
        data, addr = client_sockfd.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 创建新的进程
    process_id = os.fork()
    if process_id < 0:
        sys.exit("ERROR!")
    elif process_id == 0:
        send_msg(client_sockfd, name)
    else:
        recv_msg(client_sockfd)

    client_sockfd.close()


# 寻找网络
def search():
    client_sockfd = socket.socket(type=socket.SOCK_DGRAM)
    msg = "L " + '管理员'
    for i in range(131, 255):
        server_address = ('176.23.6.' + str(i), 8888)
        client_sockfd.sendto(msg.encode(), server_address)
        data, addr = client_sockfd.recvfrom(1024)
        print(data.decode())
        if data:
            print(addr)


if __name__ == '__main__':
    search()















