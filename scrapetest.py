from urllib2 import urlopen
html = urlopen( "http://www.pythonscraping.com/pages/page1.html")
print( html. read( ) )