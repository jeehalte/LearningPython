import urllib2
import sys

url = sys.argv[1]
request = urllib2.Request(url)
response = urllib2.urlopen(request)

print response.read()