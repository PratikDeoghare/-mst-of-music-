# encoding: utf-8

from bs4 import BeautifulSoup
import re

data = open('engenremap.html').read()

soup = BeautifulSoup(data, 'html5lib')

def f(x, txt):
    return filter(unicode.isdigit, re.findall(x + ': [0-9]+px;', txt)[0])

i = 0
for div in soup.find_all('div', id = re.compile('item')):
    top = f('top', div.get('style')) 
    left = f('left', div.get('style'))
    print '%d, %s, %s, %s'%(i, top, left, div.text[:-2])
    i = i + 1
