#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 1024

int main() {
    // Detalhes do servidor e da conexão
    std::string serverIP = "smtp.example.com";
    int serverPort = 25;  // Porta SMTP padrão

    // Informações do destinatario e do remetente
    std::string senderEmail = "sender@example.com";
    std::string recipientEmail = "recipient@example.com";

    // Info da mensagem
    std::string subject = "Hello from C++ SMTP"; //assunto
    std::string message = "This is the body of the email."; //conteudo

    // Conexão com o servidor SMTP
    int sockfd;
    struct sockaddr_in serverAddr;
    char buffer[BUFFER_SIZE];

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        std::cerr << "Não foi possivel conectar o socket." << std::endl;
        return 1;
    }

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(serverPort);
    serverAddr.sin_addr.s_addr = inet_addr(serverIP.c_str());

    if (connect(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        std::cerr << "Falha ao conectar." << std::endl;
        return 1;
    }

    // Resposta do servidor
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    //comandos do protocolo

    // Send HELO/EHLO command
    std::string heloCommand = "HELO localhost\r\n";
    send(sockfd, heloCommand.c_str(), heloCommand.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    // Send MAIL FROM command
    std::string mailFromCommand = "MAIL FROM: <" + senderEmail + ">\r\n";
    send(sockfd, mailFromCommand.c_str(), mailFromCommand.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    // Send RCPT TO command
    std::string rcptToCommand = "RCPT TO: <" + recipientEmail + ">\r\n";
    send(sockfd, rcptToCommand.c_str(), rcptToCommand.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    // Send DATA command
    std::string dataCommand = "DATA\r\n";
    send(sockfd, dataCommand.c_str(), dataCommand.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    // Send email content
    std::string emailContent = "Subject: " + subject + "\r\n\r\n" + message + "\r\n.\r\n";
    send(sockfd, emailContent.c_str(), emailContent.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    // Send QUIT command
    std::string quitCommand = "QUIT\r\n";
    send(sockfd, quitCommand.c_str(), quitCommand.size(), 0);
    recv(sockfd, buffer, BUFFER_SIZE, 0);
    std::cout << buffer << std::endl;

    return 0;
}
