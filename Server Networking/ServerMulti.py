"""
This is the server network code that runs on a raspberry pi, the default host ip is localhost, the default port is 8888. The client
uses the port 8888 to connect and goes through the dns gamertime.ddns.net which was used by Jacob when developing and showing
off the game. This server recieves data and shares it with everyone
"""

from socket import *
from threading import Thread
import queue

def clientHandler(q, s): # This is code that handles each player
    conn, addr = s.accept() # Connection is accepted by an ip address
    print(addr, "is Connected")
    
"""
This section of code handles the data that is sent to and sent from the server. It starts with a loop that trys to run the inside code.
This code recieves data, decodes it, shares it to the queue, reads the lastest thing in the queue, and sends the data to the client.
"""

    while True:
        try:
            data = conn.recv(1024) # Recieves Data from the client
            if not data: #  If the data recieved is instead a termination message, the socket is closed, and the code breaks the loop
                s.close()
                print(addr, "has Disconnected")
                break
            print("Received Message", repr(data)) # Prints what data was recieved
            print("Sharing Data")
            share = q.get() # Reads the most recent shared data before sharing so that it gets other data than itself
            print(share)
            q.put(data) # Shares own data to the queue
            print("Sending Message" + str(share))
            reply = str(share)
            conn.sendall(reply.encode()) # sends encoded, shared data to the client
        except:
            print("Connection Terminated")
            
"""
HOST is the host's ip address where the default '' is localhost. PORT is the port that the game uses to get connections from,
the default is 8888 which the client also uses. PLAYERS sets the number of how many threads get created, each handling one
instance of a player. Unintentionally and unable to be fixed (as far as I know) if a player leaves than that thread crashes.
"""

HOST = ''
PORT = 8888
PLAYERS = 100

q = queue.Queue() # This section sets up a queue to handle data sharing between threads, default fills it with nothing
q.put("")

print("Server is Starting")
try:
    s = socket(AF_INET, SOCK_STREAM) # This section sets up the server by binding to the port and listens for connections
    s.bind((HOST, PORT))
    s.listen(PLAYERS)
    print("Server has started.")
except:
    print("Error starting server.")

for i in range(PLAYERS): # This code creates the number of threads that the PLAYERS variable equals (default 100)
    Thread(target=clientHandler, args=(q, s)).start()

s.close()
