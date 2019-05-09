import socket

class send(wizard = "b", username = "Bob", xCoord = 20, yCoord = 20):
def main():
    host = '192.168.2.42'
    port = 8888
    name = username
    wiz = wizard
    x = xCoord
    y = yCoord

    mySocket = socket.socket()
    mySocket.connect((host, port))

    while True:
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    mySocket.close()


main()
