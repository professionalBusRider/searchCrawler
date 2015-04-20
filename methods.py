import jinja2
import os

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

#returns the number of times keyWord is in wordArray
def getWordCount(wordArray,keyWord):
	occuranceStrict = 0
	occuranceSoft = 0
	for word in wordArray:
		if word == keyWord:
			occuranceStrict+=1
		if word.find(keyWord) != -1:
			occuranceSoft+=1
	return occuranceStrict, occuranceSoft

#returns content within <title>
def getTitle(pageSource):
	soup = BeautifulSoup(pageSource)
	return soup.title

#returns page source of url
def getPage(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return "NULLPAGESOURCE"

def getRender(dataPackage):
	loader = jinja2.FileSystemLoader(os.getcwd())
	environment = jinja2.Environment(loader=loader, trim_blocks = True, lstrip_blocks = True)
	template = environment.get_template('template.html')
	render = template.render(title = 'title braaahh', allUrls = dataPackage[0])
	return render