from socket import *

server_address = ('localhost', 65535)
sckt = socket(AF_INET, SOCK_DGRAM)
print('starting up on \033[1;35;m%s \033[1;37;mport \033[1;35;m%s \033[1;37;m' % server_address)
sckt.bind(server_address)

timeout = 20
try:
    while True:
        print('Waiting to receive message\n')
        data, addr = sckt.recvfrom(4096)

        print('receive \033[1;35;m%s \033[1;37;mdata from \033[1;35;m%s \033[1;37;m' % (len(data), addr))
        print(data)

        if data:
            sent = sckt.sendto(data, addr)
except error:
    print("\033[1;31;mCould not open socket error:\033[1;37;m %s"% (error))
finally:
    print('Server stopped!')
    sckt.close()
