import socket
import threading
import colorama
from colorama import Fore, Back, Style

colorama.init()
print(Fore.RED)
print(" ██████╗██╗  ██╗ █████╗ ████████╗██╗    ██╗███████╗██████╗ ")
print("██╔════╝██║  ██║██╔══██╗╚══██╔══╝██║    ██║██╔════╝██╔══██╗")
print("██║     ███████║███████║   ██║   ██║ █╗ ██║█████╗  ██████╔╝")
print("██║     ██╔══██║██╔══██║   ██║   ██║███╗██║██╔══╝  ██╔══██╗")
print("╚██████╗██║  ██║██║  ██║   ██║   ╚███╔███╔╝███████╗██████╔╝")
print(" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚═════╝ ")
       

nickname = input("Kullanıcı Girin: ")

#client.connect Enter the active tunnel service ip and port in the section
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('7.tcp.eu.ngrok.io', 17890))
def receive():
    while True:
        try:
            
            
            message = client.recv(1024).decode("utf-8")
            if message == 'NICK':
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
             
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode("utf-8"))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
