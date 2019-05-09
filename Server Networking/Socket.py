""" Wizard Tower Server-side Code"""
import socket
import sys


def main():
    host = ""   # Sets the host address to the default
    port = 8888 # Sets the port to 8888 which is port forwarded
    players = 100    # Sets the number of players

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Creates the socket
    print ('Socket has been created')

    try:    # Tries to bind to the socket, if it fails then it reports the error message
        mySocket.bind((host, port))
    except socket.error as message:kn
        print ('Bind failed. Error Code : ' + str(message[0]) + ' Message ' + message[1])
        sys.exit()
    print('Socket binding has been completed successfully.')

    mySocket.listen(players) # This states how many people are allowed to join
    conn, adr = mySocket.accept()   # Allows for connections
    print("Connection from: " + str(adr))
    while True: # This section handles data de/encoding and sending
        data = conn.recv(1024).decode()
        if not data:
            print("No data Recieved")
        print("From connected User: " + str(data))

        print("Sending: " + str(data))
        conn.send(data.encode())

    conn.close()

main()
