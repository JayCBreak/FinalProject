# An example script to connect to Google using socket
# programming in Python
import socket


def Main():
    host = '69.157.26.203'
    port = 8888

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" -> ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print ('Received from server: ' + data)

        message = input(" -> ")

    mySocket.close()


if __name__ == '__main__':
    Main()
