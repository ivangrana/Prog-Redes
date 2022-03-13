import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username=input("Usuário:")

password = getpass()


try:
    resposta = requests.get('https://www.google.com',auth=HTTPBasicAuth(username,password))

    print('Codigo de resposta: %' %str(resposta.status_code))

    if resposta.status_code == 200:
     print('Login Realizado com sucesso :' + resposta.text)

except:
    print("Não foi possível realizar o login")
