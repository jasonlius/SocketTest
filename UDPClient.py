from socket import *

serverName = 'www.jasonliu1999.top'
serverPort = 12000
clientSocket = socket(AF_INET , SOCK_DGRAM)
message = input("Enter a piece of message : ")
clientSocket.sendto(message.encode(),(serverName,serverPort))
revMess, serverAddr = clientSocket.recvfrom(2048)
print(revMess.decode())
clientSocket.close()
