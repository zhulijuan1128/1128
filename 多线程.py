import socket
from threading import Thread
PORT = 6000
HOST = '192.168.13.74'
def send(sock, addr):
    i_say = ''
    while i_say != 'bye':
        i_say = input('i say:')
        sock.sendto(i_say.encode('utf8'),addr)

def recv(sock):
    while True:
        pass
        other_say, addr = sock.recvfrom(1024)
        print('{} say> {}'.format(addr[0],
                                  other_say.decode('utf-8')))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    ipaddr = input('you want say to (ip):')
    addr = (ipaddr, 6000)

    sendTH = Thread(target=send, args=(s, addr))
    sendTH.setDaemon(True)
    sendTH.start()
    recvTH = Thread(target=recv, args=(s,))
    recvTH.setDaemon(True)
    recvTH.start()
    sendTH.join()
    recvTH.join()