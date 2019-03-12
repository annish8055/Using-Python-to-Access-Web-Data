import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysocket.close()

#Date: Tue, 12 Mar 2019 06:47:06 GMT
#Server: Apache/2.4.18 (Ubuntu)
#Last-Modified: Sat, 13 May 2017 11:22:22 GMT
#ETag: "1d3-54f6609240717"
#Accept-Ranges: bytes
#Content-Length: 467
#Cache-Control: max-age=0, no-cache, no-store, must-revalidate
#Pragma: no-cache
#Expires: Wed, 11 Jan 1984 05:00:00 GMT
#Connection: close
#Content-Type: text/plain
