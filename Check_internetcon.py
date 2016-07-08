import urllib2

try:
	urllib2.urlopen("http://google.com", timeout=2)
	print "Internet connection is active!"

except urllib2.URLError:
	print "No internet connection"
