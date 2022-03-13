import http.client

conexao = http.client.HTTPConnection("www.google.com")

conexao.request("GET", "/")

resposta = conexao.getresponse()

print(type(resposta))

print(resposta.status, resposta.reason)

if resposta.status == 200:
    data = resposta.read()

