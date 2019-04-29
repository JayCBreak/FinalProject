""" Wizard Tower Socket
Open Command Prompt
ssg and ipconfig"""
import socket
import sys

HOST = ''   # All available interfaces
PORT = 8888 # Any non-privileged port *can only be used once (cannot make the same port twice) 8888 and 8889 are used

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket has been created')

#Used to bind socket to localhost and port
try:
    s.bind((HOST, PORT))
except socket.error as message:
    print ('Bind failed. Error Code : ' + str(message[0]) + ' Message ' + message[1])
    sys.exit()

print ('Socket binding has been completed')

#Used to start listening on socket
s.listen(10)  #number of people that can be on the server
print ('Socket is now listening')

#Lets talk with the client
while 1:
    #Accept a connection - blocking call
    conn, adr = s.accept()
    print ('Connected with ' + adr[0] + ':' + str(adr[1]))

s.close()

import socket
import sys

HOST = ''   # All available interfaces
PORT = 8888 # Any non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket has been created')

#Used to bind socket to localhost and port
try:
    s.bind((HOST, PORT))
except socket.error as message:
    print ('Bind failed. Error Code : ' + str(message[0]) + ' Message ' + message[1])
    sys.exit()

print ('Socket binding has been completed')

#Used to start listening on socket
s.listen(10)  #Max number of computers able to connect
print ('Socket is now listening')

#Lets talk with the client
while 1:
    #Accept a connection - blocking call
    conn, adr = s.accept()
    print ('Connected with ' + adr[0] + ':' + str(adr[1]))

s.close()
