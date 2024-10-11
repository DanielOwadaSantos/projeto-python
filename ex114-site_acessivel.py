import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('Este site não está acessível no momento!')
else:
    print('Site acessado com sucesso!')
    print(site.read()) # Comado usado para acesar conteúdo html do site que acabou de aceassar
