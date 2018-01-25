import urllib2
from bs4 import BeautifulSoup

# open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

print webpage

print BeautifulSoup(webpage)
# comments
