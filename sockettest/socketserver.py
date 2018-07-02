import socket
import csockthread
import threading
import os

if __name__ == '__main__':
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.gethostname(), '\nsockinfo--', serversock)
    print('server::pid--', os.getpid(),
          '--mainthread--', threading.get_ident())

    serversock.bind(('localhost', 8009))
    serversock.listen(126)

    while True:
        (clientsock, address) = serversock.accept()
        print('\n\nserver::connected.address--', address)
        ct = csockthread.Csthread(clientsock)
        ct.start()
