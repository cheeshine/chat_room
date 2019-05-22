"""

"""
import socket
import os, sys

# 服务器地址
# host_address = ('0.0.0.0', 8889)
host_address = ('176.23.6.118', 8888)


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
        print(data.decode() + '\n发言:', end='')


# 创建网络连接
def main():
    client_sockfd = socket.socket(type=socket.SOCK_DGRAM)
    while True:
        name = input('请输入姓名：')
        # name = '蔡徐坤'
        msg = "L " + name
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


if __name__ == '__main__':
    server_ip = '176.23.6.'
    server_ip += input('请输入IP:')
    server_port = int(input('请输入PORT:'))
    host_address = (server_ip, server_port)
    main()










