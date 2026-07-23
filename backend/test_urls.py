import urllib.request
import urllib.error

try:
    urllib.request.urlopen('http://127.0.0.1:8000/api/')
except urllib.error.HTTPError as e:
    with open('django_404.html', 'w') as f:
        f.write(e.read().decode('utf-8'))
