#page = 'asdfasdfias dfasdiuf asdifb sadfubfsd <a href="http://duck.com"> asdfasdf'
#start_link = page.find('<a href=')
#start_quote = page.find('"', start_link)
#end_quote = page.find('"', start_quote+1)
#url = page[start_quote+1:end_quote]
#print(url)	

#def getURL(page):
#	start_link = page.find('<a href=')
#	if start_link == -1:
#		return None, 0
#	start_quote = page.find('"', start_link)
#	end_quote = page.find('"', start_quote+1)
#	url = page[start_quote+1:end_quote]
#	return url, end_quote
#
#url, nextPos = getURL('asdfasdfasd<a href="http://duck.com"> as')
#if url:
#	print url
#else:
#	print 'none'


#def printAll(page):
#	while True:
#		url, endPos = getURL(page)
#		if url:
#			print url
#			page = page[endPos:]
#		else:
#			break
#
#def getAllLinks(page):
#	links = []
#	while True:
#		url, endPos = getURL(page)
#		if url:
#			links.append(url)
#			page = page[endPos:]
#		else:
#			return links
#			#break
#
#def crawl_web(seed):
#	tocrawl = [seed]
#	crawled = []
#	while tocrawl:
#		page = tocrawl.pop()
#		if page not in crawled:
#			crawled.append(page)
#			union(tocrawl,getAllLinks(page))
#			#tocrawl += getAllLinks(page)
#		return crawled
#
def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""

print get_page("https://www.google.com/")

#print get_page('http://xkcd.com/353')
#print crawl_web('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')

#printAll('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')
