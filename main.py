import userio

searchTerms = userio.getInput()

allUrls = userio.getUrls(searchTerms)
print 'found urls, now searching...'
dataPackage = userio.getDataPackage(allUrls)

userio.renderPage(dataPackage)