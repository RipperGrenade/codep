import threading
import socket
import os
import urllib.request
import select


class Csthread(threading.Thread):
    __nodeurl_ = 'http://localhost:3000'
    __pid_ = None
    __data_ = 'this is a message from socket server'

    def __init__(self, csocket: socket.socket):
        threading.Thread.__init__(self, daemon=True)
        self.csocket = csocket
        self.__pid_ = os.getpid()

    def run(self):
        print('\n\nsthread::pid--', self.__pid_)
        print('sthread::sock thread running--', self.csocket.getpeername(), '--', threading.get_ident())

        self.send()
        self.nonblksend()
        try:
            resp = urllib.request.urlopen(self.__nodeurl_)
            html = resp.read()
            print('sthread::connecting to nodeserver')
            for line in html.splitlines():
                print('html--', line.decode('utf-8'))
        except urllib.error.URLError as urlerr:
            print('err::', urlerr, '--', self.__nodeurl_)
            os.kill(self.__pid_, 9)

        self.csocket.close()

    def nonblksend(self):
        self.csocket.setblocking(False)
        socketfd = self.csocket.fileno()
        print('sthread::nonblcksocket fd--', socketfd, '--', self.csocket.getsockname())
        potential_readers = [self.csocket]
        potential_writers = [self.csocket]
        potential_errs = [self.csocket]
        recvdatalst = []
        sentlen = 0
        rendflag = False
        wendflag = False
        while True:
            if rendflag and wendflag:
                print('end of r and w')
                break
            ready_to_read, ready_to_write, in_error = \
                select.select(potential_readers, potential_writers, potential_errs, None)
            if ready_to_read.__len__() > 0:
                print('nonblck::readyread--')
                recvdata = ready_to_read[0].recv(10)
                if recvdata == b'':
                    print('nonblck::sock connection closed')
                    rendflag = True
                if b'ok' in recvdata:
                    print('nonblck::succed sent==', recvdata.decode('utf-8'))
                    recvdatalst.append(recvdata.decode('utf-8'))
            if ready_to_write.__len__() > 0:
                if sentlen < self.__data_.__len__():
                    print('nonblck::readysent--')
                    tmp = self.__data_[sentlen] + '--nblk'
                    sent = ready_to_write[0].send(tmp.encode('utf-8'))
                    if sent == 0:
                        raise RuntimeError("nonblck::socket connection broken")
                    sentlen += 1
                    print('nonblck::sent--', tmp)
                elif sentlen == self.__data_.__len__():
                    sentlen += 1
                    print('nonblck::readysent--EOS')
                    sent = ready_to_write[0].send('EOS'.encode('utf-8'))
                    if sent == 0:
                        raise RuntimeError("nonblck::socket connection broken")
                    wendflag = True
                    # print('csthread::potential_errs--', potential_errs)
        print('csthread::nonblocking--receiv', ''.join(recvdatalst))

    def send(self):
        bytecnt = 0
        for char in self.__data_:
            byteschar = str.encode(char, 'utf-8')
            sent = self.csocket.send(byteschar)
            print('sent val::', sent)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            recvdata = self.csocket.recv(1)
            print('recv val', recvdata)
            if b'ok' in recvdata:
                print('succed sent==', recvdata.decode('utf-8'))
            bytecnt += byteschar.__len__()
            print('sockserver::message sent, bytelength=={0}'.format(bytecnt))
        # self.csocket.close()
