from socket import *
from datetime import datetime

server_addres = ('127.0.0.1', 65535)
message = []
nickname = 'LSD'
def log(message):
     now = datetime.now().strftime('%H:%M:%S ')
     return now+ message
try:
    sckt = socket(AF_INET, SOCK_DGRAM)
    sckt.connect(server_addres)
    message_lenght = 0
    x = 0
    for x in range(t):
        gm = input(':')
        message.insert(x, gm)
        #print(log('%s: %s'% (nickname, message[x])))
        message_lenght += len(message[x])
        sent = sckt.sendto(bytes(log(nickname+ ': '+ message[x]), 'utf-8'), server_addres)
        data, server = sckt.recvfrom(4096)
        print(data.decode())
    print(log('Send \033[1;35;m%s\033[1;37;m data to \033[1;35;m%s \033[1;37;m' % (message_lenght, server_addres)))
except error:
        print("\033[1;31;mCould not open socket error:\033[1;37;m %s"% (error))
        sckt.close()
finally:
    print("Closing socket")
    sckt.close()
