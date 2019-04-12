from socket import *

server_addres = ('127.0.0.1', 65535)
message = []
t = 3
sckt = socket(AF_INET, SOCK_DGRAM)
try:
    message_lenght = 0
    x = 0
    for x in range(t):
        gm = input(':')
        message.insert(x, gm)
        message_lenght += len(message[x])
        sent = sckt.sendto(bytes(message[x], 'utf-8'), server_addres)
        data, server = sckt.recvfrom(4096)
    print('Send \033[1;35;m%s\033[1;37;m data \033[1;35;m%s \033[1;37;mtimes to \033[1;35;m%s \033[1;37;m' % (message_lenght, x+1, server_addres))
except error:
        print("\033[1;31;mCould not open socket error:\033[1;37;m %s"% (error))
        sckt.close()
finally:
    print("Closing socket")
    sckt.close()
