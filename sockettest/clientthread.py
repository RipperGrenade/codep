import threading
import socket
import select
import struct


class Nblkthread(threading.Thread):
    def __init__(self, sock: socket.socket, serveraddr, senddatalst):
        threading.Thread.__init__(self)
        self._csock = sock
        self._addr = serveraddr
        self._recvlst = []
        self._senddata = senddatalst

    def run(self):
        self._csock.connect(self._addr)
        print('Nblkthread::--', self._csock.getsockname())
        sentidx = 0
        endr = False
        endw = False
        rdata = []
        while True:
            endt = endr and endw
            if endt is True:
                print('Nblkthread::end of r and w')
                break
            rlist, wlist, errlist = select.select([self._csock], [self._csock], [self._csock], None)
            rstr = ''.join(rdata)
            if 'EOS' in rstr:
                print('Nblkthread::receive end')
                endr = True
            elif rlist.__len__() > 0:
                print('Nblkthread::read ready--')
                recvdata = self._csock.recv(10)
                if b'' == recvdata:
                    print('Nblkthread::sock connection closed')
                    break
                rdata.append(recvdata.decode('utf-8'))
                print('Nblkthread::recevd--', recvdata)

            if wlist.__len__() > 0 and endw is False:
                print('Nblkthread::send ready--')
                if sentidx < self._senddata.__len__():
                    data = self._senddata[sentidx]
                    if isinstance(data, int):
                        sdat = struct.pack('h', data)
                        if self._csock.send(sdat) == 0:
                            raise RuntimeError('Nblkthread::sock connection broken')
                    elif isinstance(data, str):
                        for char in data:
                            schar = struct.pack('h', ord(char))
                            sent = self._csock.send(schar)
                            if sent == 0:
                                raise RuntimeError('Nblkthread::sock connection broken')
                            print('Nblkthread--sentbyte::--', schar)
                    sentidx += 1
                    print('Nblkthread--sent::--', data)
            if sentidx == self._senddata.__len__():
                endw = True
                sentidx = 0
                print('Nblkthread::end sent')
