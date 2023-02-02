#include <arpa/inet.h> // inet_addr()
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h> // 
#include <sys/socket.h>
#include <unistd.h> // 
#define MAX 80
#define PORT 9998
#define SA struct sockaddr

// funcao responsavel por enviar a mensagem ao server
void mandar_mensagem(int sockfd) 
{
	
	char buff[MAX];
	int n;
	for (;;) {
		bzero(buff, sizeof(buff));
		printf("Insira a mensagem : ");
		n = 0;
		while ((buff[n++] = getchar()) != '\n')
			;
		write(sockfd, buff, sizeof(buff));
		bzero(buff, sizeof(buff));
		read(sockfd, buff, sizeof(buff));
		printf("Server : %s", buff);
		if ((strncmp(buff, "exit", 4)) == 0) {
			printf("Cliente saindo...\n");
			break;
		}
	}
}

int main()
{
	int sockfd, connfd;
	struct sockaddr_in servaddr, cli;

	// socket create and verification
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd == -1) {
		printf("Falha ao criar o socket...\n");
		exit(0);
	}
	else
		printf("Socket criado !...\n");
	bzero(&servaddr, sizeof(servaddr));

	// assign IP, PORT
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servaddr.sin_port = htons(PORT);

	// conexao do client com o servidor
	if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr))
		!= 0) {
		printf("Erro ao conectar com o servidor...\n");
		exit(0);
	}
	else
		printf("Conectado ao server..\n");

	// function for chat
	mandar_mensagem(sockfd);

	// close the socket
	close(sockfd);
}