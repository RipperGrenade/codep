import socket
import ssl
import os
import tlst.tlsthread as tls

hostname = 'localhost'
port = 10443

server_cert = 'servercert/python-tls-server-cert.pem'
server_key = 'servercert/python-tls-server-key.pem'

# optional
client_cert = 'servercert/clientcert_toconnect/nodejs-tls-client-cert.pem'

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

# optional
context.load_verify_locations(cafile=client_cert)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tlssock = context.wrap_socket(tcpsock, server_side=True)
tlssock.bind((hostname, port))
tlssock.listen(100)

data = 'this is tls server saying hello'
print('PID::', os.getpid())
while True:
    (sslsock, info) = tlssock.accept()
    thrd = tls.TLSThread(sslsock, data)
    thrd.start()
