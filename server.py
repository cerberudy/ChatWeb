import socket
import time
import threading
import colorama 
from colorama import Fore, Back, Style

colorama.init()
print(Fore.RED)
print("Bağlantı kurulduğunda sohbet başlayacaktır...")
time.sleep(1)
print("Chat will start when users connect... ")
time.sleep(1)
print(Fore.YELLOW)
print("...")
time.sleep(2)
print(Fore.RED)
print("Bağlantı kuruluyor...#")
time.sleep(1)
print("Establishing connection...#")

#tünel servisini 5555 port'u ile açın
#open tunnel service with port 5555
host = '127.0.0.1'
port = 5555


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            
            message = client.recv(1024)
            broadcast(message)
        except:
            
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode("utf-8"))
            nicknames.remove(nickname)
            break
def receive():
    while True:
         
        client, address = server.accept()
        print(Fore.YELLOW)
        print("Bağlantı kuruldu {}".format(str(address)))

         
        client.send('NICK'.encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(Fore.BLUE) 
        print("Kullanıcı {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode("utf-8"))
        client.send('Connected to server!'.encode("utf-8"))

        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
