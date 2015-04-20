import methods
from pygoogle import pygoogle

def getInput():
	searchTermsString = raw_input("search terms: ")
	searchTerms = []
	searchTerms = searchTermsString.split(',')
	return searchTerms

def getUrls(searchTerms):
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

	return allUrls

def getDataPackage(allUrls):
	dataPackage = []
	wordCountSubPackage = []
	wordCountStrictSubPackage = []
	wordCountSoftSubPackage = []

	for websites in allUrls:
		for website in websites:
			pageSource = methods.getPage(website)
			#if the source of the page was able to load
			if pageSource != 'NULLPAGESOURCE':
				wordArray = methods.getWordArray(pageSource)
				wordCountStrict, wordCountSoft = methods.getWordCount(wordArray, "medical")
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

	return dataPackage

def renderPage(dataPackage):
	render = methods.getRender(dataPackage)
	htmlFile = open("/var/www/html/main.html","wb")
	htmlFile.write(render)
	htmlFile.close()
