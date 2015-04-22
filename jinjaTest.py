#from jinja2 import Template
#template = Template('Hello {{ name }}!')
#print template.render(name='John Doe')

#from jinja2 import Environment, PackageLoader
#environment = Environment(loader=PackageLoader('/home/wyatt/python/webCrawler', 'templates'))
#template = environment.get_template('template.html')
#print template

import jinja2
import os

list = ['a','b','c','eee']

loader = jinja2.FileSystemLoader(os.getcwd())
environment = jinja2.Environment(loader=loader, trim_blocks = True, lstrip_blocks = True)
template = environment.get_template('template.html')
render = template.render(title = 'aaabbb', list = list)

print render