#Senha e email do remetente
    remetente = 'devscrappers@outlook.com'
    senha = ''
    destinatario = mail 
#MIME
    message = MIMEMultipart()
    message['From'] = remetente
    message['To'] = destinatario
    message['Subject'] = 'links raspados'   #Assunto do email
#corpo e anexos
    message.attach(MIMEText(mail_content, 'plain'))
#Criação da sessão SMTP
    s = smtplib.SMTP('smtp.office365.com', 587) #porta 587 do hotmail
    s.starttls() #TLS
    s.login(remetente, senha) #fazendo o login...
    text = message.as_string()
    s.sendmail(remetente, destinatario, text)
    s.quit()
    print('Email enviado')
