import socket
import sys

domain = ''
port = 80

print(sys.argv)
if len(sys.argv) > 1:
    domain = sys.argv[1]

if len(sys.argv) > 2:
    port = int(sys.argv[2])

destination = (domain, port)

print(destination)

request = b'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close'

socks = socket.socket()
socks.connect(destination)
