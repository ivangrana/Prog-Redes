#Criação de um servidor utilizando o protocolo TCP
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9998
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP,SERVER_PORT))
server.listen(5)
print("[*] Server em modo escuta %s:%d" % (SERVER_IP,SERVER_PORT))
client,addr = server.accept()
client.send("Aceitando conexão...".encode())
print("[+] Conexão aceita com: %s:%d" %(addr[0],addr[1]))

def request_cliente(client_socket:socket.socket):
    """Função responsável por receber a mensagem do cliente no servidor"""
    request = client_socket.recv(1024)
    request = bytes(request)
    print("[+] Mensagem recebida: %s do usuário %s" %(request.decode('UTF-8'), client_socket.getpeername()))
    client_socket.send(bytes("ACK ","utf-8"))
    client_socket.send(bytes("Mensagem envida com sucesso !\n","utf-8"))
    

while True:
    request_cliente(client)   
        
    
