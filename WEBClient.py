from socket import *

serverName = '192.168.116.137'
serverPort = 6666
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = raw_input('Input filename you want to download:')
clientSocket.send(message.encode('utf-8'))
modifiedMessage  = clientSocket.recv(4096)
print 'From Server:\n\n', modifiedMessage
contentlen =  int(modifiedMessage[modifiedMessage.find("Content-Length")+16:])
content = ""
for i in range(0, contentlen):
    content += clientSocket.recv(4096)
print str(content)
clientSocket.close()
