#import the module httplib2
import httplib2

#import module BeautifulSoup
from BeautifulSoup import BeautifulSoup, SoupStrainer


http = httplib2.Http()

status, response = http.request('your link')

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_key('href'):
        print link['href']
