from pygoogle import pygoogle
#WARNING pygoogle can only get a small amount of searches per time interval

#searchTerms: array of items to google
#allUrls: array of arrays of google urls

#getting user input
searchTermsString = raw_input("search terms: ")
searchTerms = []
searchTerms = searchTermsString.split()

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







#g = pygoogle('Abbvie')
#g.pages = 1
#print '*Found %s results*'%(g.get_result_count())
#print g.get_urls()