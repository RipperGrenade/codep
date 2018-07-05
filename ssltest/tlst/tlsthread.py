import threading
import ssl


class TLSThread(threading.Thread):
    def __init__(self, tlssock: ssl.socket, data):
        threading.Thread.__init__(self)
        self._tlssock = tlssock
        self._data = data

    def run(self):
        print('tlsthread-----peercert::', self._tlssock.getpeercert())
        self._tlssock.setblocking(0)
        sent = self._tlssock.send((self._data + 'EOS').encode('utf-8'))
        if sent == 0:
            raise RuntimeError('tls connection broken')
        print('sent::', self._data)
