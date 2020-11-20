import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
position = int(input('Position:'))
repeat = int(input('Repeat:'))
a ="hello"
links = list()

for i in range(repeat):
	print(a)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	tags = soup('a')
	for tag in tags:
		links.append(tag.get('href', None))
	print(links[0:position])
	d = links[position-1]
	print(d)
	url=str(d)

    	
