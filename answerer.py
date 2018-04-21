import urllib.request
import urllib.parse

url = 'https://www.google.com/search?q={}'
searchterm = ''
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))