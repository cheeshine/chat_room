"""
    Chat Room
    env: 3.6.7
"""
import socket
import os

# 服务器地址
# host_address = ('0.0.0.0', 8889)
host_address = ('176.23.6.118', 8888)
# 存储用户信息
user = {}


# 进入聊天室
def do_login(server_sockfd, name, address):
    if name in user or "管理员" in name:
        server_sockfd.sendto("该用户已存在".encode(), address)
        return
    server_sockfd.sendto(b'OK', address)

    # 通知其他人
    msg = "欢迎%s进入聊天室" % name
    for i in user:
        server_sockfd.sendto(msg.encode(), user[i])

    # 将用户加入
    user[name] = address


def do_chat(server_sockfd, name, text):
    msg = "%s : %s" % (name, text)
    for i in user:
        if i != name:
            server_sockfd.sendto(msg.encode(), user[i])


def do_quit(server_sockfd, name):
    msg = "%s退出了聊天室" % name
    for i in user:
        if i != name:
            server_sockfd.sendto(msg.encode(), user[i])
        else:
            server_sockfd.sendto(b'EXIT', user[i])

    # 将用户删除
    del user[name]


# 接受各种客户端请求
def do_request(server_sockfd):
    while True:
        data, client_address = server_sockfd.recvfrom(1024)
        # print(data.decode())
        msg = data.decode().split(' ')
        # 区分请求类型
        if msg[0] == 'L':
            do_login(server_sockfd, msg[1], client_address)
        elif msg[0] == 'C':
            text = ' '.join(msg[2:])
            do_chat(server_sockfd, msg[1], text)
        elif msg[0] == 'Q':
            if msg[1] not in user:
                continue

            do_quit(server_sockfd, msg[1])


# 创建网络连接
def main():
    # 套接字
    server_sockfd = socket.socket(type=socket.SOCK_DGRAM)
    server_sockfd.bind(host_address)

    process_id = os.fork()
    if process_id < 0:
        return
    # 发送管理员消息
    elif process_id == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            server_sockfd.sendto(msg.encode(), host_address)

    else:
        # 请求处理
        do_request(server_sockfd)  # 处理客户端请求


if __name__ == '__main__':
    main()






