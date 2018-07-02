import socket
import os
import clientthread

if __name__ == '__main__':
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsock.connect(('localhost', 8009))
    print('\n\nclient::pid--{0},connetd--info:local=={1},remote=={2}'.format(os.getpid(), clientsock.getsockname(),
                                                                             clientsock.getpeername()))
    recvdata = []
    while True:
        tmp = clientsock.recv(10)
        if tmp is not None:
            print('sockclient::piece recev', tmp.decode('utf-8'))
            ackok = tmp.decode('utf-8') + '--ok'
            sent = clientsock.send(ackok.encode('utf-8'))
            if sent == 0:
                raise RuntimeError('sockclient::sock connection broken')
        if tmp == b'':
            print('sock connection closed')
            break
        recvdata.append(tmp.decode('utf-8'))
        if 'EOS' in recvdata:
            print('server end of sending')
            break

    print('blocking::sockclient::received--', ''.join(recvdata))

    nonblksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    saddr = ('localhost', 8009)
    data = ['hello', 'world', 1, 35, 89, 255, 'python']
    thrd = clientthread.Nblkthread(nonblksock, saddr, data)
    thrd.start()
