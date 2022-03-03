#Criação de um servidor utilizando o protocolo TCP

import socket
import threading
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9998
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP,SERVER_PORT))
server.listen(5)
print("[*] Server em modo escuta %s:%d" % (SERVER_IP,SERVER_PORT))
client,addr = server.accept()
client.send("Aceitando conexão...".encode())
print("[*] Conexão aceita com: %s:%d" %(addr[0],addr[1]))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Pedido aceito: %s do cliente %s" , request, client_socket.getpeername())
    client_socket.send(bytes("ACK","utf-8"))
    while True:
        handle_client(client)   
        
    client_socket.close()
    server.close()
