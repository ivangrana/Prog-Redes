import socket

def info_maquina_local():   #achar informações da maquina local
    host = socket.gethostname()
    print("Nome da maquina:",host)
    host_ip = socket.gethostbyname(host)
    print("IP da maquina local:",host_ip)

def info_maquina_remota(remote_host): #achar informações de um servidor remoto
    try:
        print("IP do endereço: ",socket.gethostbyname(remote_host))
    except socket.error as mensagem_erro:
        print((remote_host, mensagem_erro))

def nome_servico(porta):    #função para achar o nome do serviço da porta
    nome_protocolo = 'tcp'
    print("nome do serviço na port",porta, "é: %s" %socket.getservbyport(porta,nome_protocolo))

def porta_servico(servico,protocolo):
    print("port: %s" %socket.getservbyname(servico,protocolo))

if __name__ == '__main__':
    info_maquina_local()
    info_maquina_remota('www.python.org')
    nome_servico(23)
    porta_servico('http','tcp')
