from email import message
from http import client
from socket import *
serverPort = 12000

serverSocket = socket(AF_INET , SOCK_DGRAM)
serverSocket.bind('',serverPort)
print("Ready to accept messages :")
while(True):
    message , clientAddr = serverSocket.recvfrom(2048)
    messageModify = message.decode().upper()
    serverSocket.sendto(messageModify.encode(),clientAddr)
    if(message.decode().upper == "QUIT"):
        serverSocket.sendto("Session Terminated ".encode(),clientAddr)
        serverSocket.close()
        break
