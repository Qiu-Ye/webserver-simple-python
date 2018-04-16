from socket import *

serverPort = 6666

serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    while True:
        print "The server is ready to receive"
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(4096)
            print message
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\ncharset=utf-8\nContent-Length: %d\n\n' %(len(outputdata))
            connectionSocket.send(header.encode('utf-8'))
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
        except IOError:
            header = 'HTTP/1.1 404 Not Found'
            connectionSocket.send(header.encode('utf-8'))
        finally:
            connectionSocket.close()
finally:
    serverSocket.close()
