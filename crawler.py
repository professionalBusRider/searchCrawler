#page = 'asdfasdfias dfasdiuf asdifb sadfubfsd <a href="http://duck.com"> asdfasdf'
#start_link = page.find('<a href=')
#start_quote = page.find('"', start_link)
#end_quote = page.find('"', start_quote+1)
#url = page[start_quote+1:end_quote]
#print(url)	

def getURL(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

#url, nextPos = getURL('asdfasdfasd<a href="http://duck.com"> as')
#if url:
#	print url
#else:
#	print 'none'


def printAll(page):
	while True:
		url, endPos = getURL(page)
		if url:
			print url
			page = page[endPos:]
		else:
			break

printAll('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')
