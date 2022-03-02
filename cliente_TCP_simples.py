import socket
import sys

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Falha ao criar o socket")
        print("Motivo: %s" %str(err))
        sys.exit();

print('Socket criado')
target_host = input("Insira o nome do servidor: ")
target_port = input("Insira a porta: ")
    
try:
        sock.connect((target_host, int(target_port)))
        print("Socket conectado a %s utilizando a porta: %s" %(target_host,target_port))
        sock.shutdown(2)
except socket.error as err:
        print("Falha ao conectar a %s na %s" %(target_host,target_port))
        print("Motivo: %s" %str(err))
        sys.exit();