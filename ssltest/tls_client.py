import socket
import ssl
# from ssl import Purpose

hostname = 'localhost'
port = 10443

# cert_loca = 'clientcert/servercert_toconnect/nodejs-tls-server-cert.pem'
cert_loca = 'clientcert/servercert_toconnect/python-tls-server-cert.pem'

cert_loca2 = 'clientcert/python-tls-client-cert.pem'
cert_locakey = 'clientcert/python-tls-client-key.pem'

saddr = (hostname, port)
# context = ssl.create_default_context(Purpose.SERVER_AUTH, cafile=cert_loca)
context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations(cafile=cert_loca)

context.load_cert_chain(certfile=cert_loca2, keyfile=cert_locakey, password=None)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tlsock = context.wrap_socket(sock, server_hostname=hostname)
tlsock.connect((hostname, port))
print('succeeded connected, tlsversion--', tlsock.version())

while True:
    recv = tlsock.recv(1024)
    if recv.__len__() > 0:
        print('recvd::', recv.decode('utf-8'))
        if 'EOS' in recv.decode('utf-8'):
            print('EOS--exit')
            break
