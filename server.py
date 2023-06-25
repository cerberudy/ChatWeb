import socket
import time
import threading

print("Bağlantı kurulduğunda sohbet başlayacaktır...")
time.sleep(1)
print("Chat will start when users connect... ")
time.sleep(1)
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
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
         
        client, address = server.accept()
        print("Bağlantı kuruldu {}".format(str(address)))

         
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

         
        print("Kullanıcı {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
