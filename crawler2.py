from pygoogle import pygoogle
from bs4 import BeautifulSoup
#WARNING pygoogle can only get a small amount of searches per time interval

#searchTerms: array of items to google
#allUrls: array of arrays of google urls

#returns array of divs based on keyWord
def findAll(pageSource,keyWord):
	soup = BeautifulSoup(pageSource)
	return soup.findAll(keyWord)

#returns array of every word in pageSource
def getWordArray(pageSource):
	soup = BeautifulSoup(pageSource)
	wordArray = []
	for sentence in soup.stripped_strings:
		words = []
		words = sentence.split()
		for word in words:
			wordArray.append(word)
	return wordArray

#returns page source of url
def getPage(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return "NULLPAGESOURCE"

#getting user input
searchTermsString = raw_input("search terms: ")
searchTerms = []
searchTerms = searchTermsString.split(',')

allUrls = []
#a way to test without query google
if('NULL' in searchTerms):
	print 'predetermined FDA search...'
	allUrls = [[u'http://www.fda.gov/', u'http://www.fda.gov/Drugs/', 
	u'http://www.fda.gov/MedicalDevices/', u'http://www.fda.gov/Safety/Recalls/', 
	u'http://en.wikipedia.org/wiki/Food_and_Drug_Administration', u'http://www.fda.com/', 
	u'https://www.facebook.com/FDA']]
else:
	for term in searchTerms:
		pygoog = pygoogle(term)
		pygoog.pages = 1
		urls = []
		urls = pygoog.get_urls()
		allUrls.append(urls)

print 'found urls, now searching...'

for websites in allUrls:
	for website in websites:
		pageSource = getPage(website)
		#if the source of the page was able to load
		if pageSource != 'NULLPAGESOURCE':
			print len(getWordArray(pageSource))
		else:
			print 'ERROR: could not load page source for: %s' % website

