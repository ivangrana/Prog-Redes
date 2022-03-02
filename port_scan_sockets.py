import socket
from threading import *

ip ='127.0.0.1' #IP das portas que serão escaneadas
lista_portas = range(1,10) #lista de portas

def scan_basico(ip,portas):
 for index in portas:
  sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  resultado = sock.connect_ex((ip,index))
  print(index,"-> %s" %resultado)
  sock.close()

def scanner_sockets(ip,portas):
    try:
        socket_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_connect.settimeout(4)
        result = socket_connect.connect((ip, portas))
        return ('%d -> tcp aberto' % portas)
    except Exception as exception:
        return ('%d -> tcp fechado' % portas)
    

for port in lista_portas:
    t = Thread(target=scanner_sockets,args=(ip,int(port)))
    t.start()