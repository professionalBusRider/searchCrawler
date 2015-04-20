import jinja2
import os

from pygoogle import pygoogle
from bs4 import BeautifulSoup

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

dataPackage = []
wordCountSubPackage = []
wordCountStrictSubPackage = []
wordCountSoftSubPackage = []

for websites in allUrls:
	for website in websites:
		pageSource = getPage(website)
		#if the source of the page was able to load
		if pageSource != 'NULLPAGESOURCE':
			wordArray = getWordArray(pageSource)
			wordCountStrict, wordCountSoft = getWordCount(wordArray, "medical")
			wordCountStrictSubPackage.append(wordCountStrict)
			wordCountSoftSubPackage.append(wordCountSoft)
			
		else:
			print 'ERROR: could not load page source for: %s' % website
			wordCountStrictSubPackage.append('N/A')
			wordCountSoftSubPackage.append('N/A')

wordCountSubPackage.append(wordCountStrictSubPackage)
wordCountSubPackage.append(wordCountSoftSubPackage)

dataPackage.append(allUrls)
dataPackage.append(wordCountSubPackage)

renderPage(dataPackage)