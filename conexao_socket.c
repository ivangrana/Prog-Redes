#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char** argv)
{
    int socket_desc;
    struct sockaddr_in server_addr;
    char server_message[2000], client_message[2000];
    
    // Clean buffers:
    memset(server_message,'\0',sizeof(server_message));
    memset(client_message,'\0',sizeof(client_message));
    
    // Criando um socket:
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    
    if(socket_desc < 0){
        printf("Não foi possivel criar o socket\n");
        return -1;
    }
    
    printf("Socket criado !\n");
    
    // configurações de conexão:
    server_addr.sin_family = AF_INET; //familia de socket
    server_addr.sin_port = htons(80); //port conectada
    server_addr.sin_addr.s_addr = inet_addr(argv[1]); //endereço IP
    
    // envio de solicitação de conexão
    if(connect(socket_desc, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0){
        printf("Não foi possivel criar o socket\n");
        return -1;
    }
    printf("Conectado ao server...\n");
    
  
    printf("Insira a mensagem: ");
    gets(client_message);
    
    
    if(send(socket_desc, client_message, strlen(client_message), 0) < 0){
        printf("Mensagem não enviada.\n");
        return -1;
    }
    
    
    if(recv(socket_desc, server_message, sizeof(server_message), 0) < 0){
        printf("Resposta não recebida\n");
        return -1;
    }
    
    printf("Resposta do servidor: %s\n",server_message);
    
    // encerra o socket:
    close(socket_desc);
    
    return 0;
}