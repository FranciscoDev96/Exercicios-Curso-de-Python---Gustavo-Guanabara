import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível')
else:
    print('O site pudim está acessível.')
    print(site.read())