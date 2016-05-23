import requests, bs4

ex = open('example.html')
es = bs4.BeautifulSoup(ex)
print(type(es))
elems = es.select('#author')
print(type(elems))
print("len "+ str(len(elems)))
print(type(elems[0]))
print(elems[0].getText())
print("str "+ str(elems[0]))