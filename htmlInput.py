import cgi
form = cgi.FieldStorage()
searchTerm = form.getvalue('SearchTerm')
keyword = form.getvalue('keyword')

print searchTerm
print keyword
print whatup