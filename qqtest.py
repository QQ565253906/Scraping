from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen( "https://user.qzone.qq.com/442986300?source=friendlist")
content = html. read( )
encoding=html.headers['content-type'].split('charset=')[-1]
ucontent = unicode(content, encoding)
print ucontent 

bsObj = BeautifulSoup( html,"html.parser" )
nameList = bsObj . findAll( "span", {"class": "green"})
#nameList = bsObj . find( "span", {"class": "green"})
for name in nameList:
	print( name. get_text( ) )
	#print( name)