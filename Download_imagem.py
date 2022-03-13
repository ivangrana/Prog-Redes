import requests

#Realizando o download de imagens de uma página utilizando Python

import urllib.request
url="https://www.python.org/static/img/python-logo.png"

urllib.request.urlretrieve(url, "python.png")

def download(url):
    with urllib.request.urlopen(url) as response:
     print("Status:", response.status)
   
    with open("python.png", "wb" ) as image:
        image.write(response.read())

if __name__ == "__main__":
    download(url)