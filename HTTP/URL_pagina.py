import requests
import re

#Extração de links e links de imagens de uma página

url = input("Inserir URL -> ")

var = requests.get(url).text

print("Links de imagens:")
for image in re.findall("<img (.*)>",var):
    for images in image.split():
        if re.findall("src=(.*)",images):
            image = images[:-1].replace("src=\"","")
        if(image.startswith("http")):
            print(image)
else:
    print(url+image)
print("Links:")
for link,name in re.findall("<a (.*)>(.*)</a>",var):
    for a in link.split():
        if re.findall("href=(.*)",a):
            url_imagem = a[0:-1].replace("href=\"","")
            if(url_imagem.startswith("http")):
                print(url_imagem)
            else:
             print(url+url_imagem)