# lucky.py - Opens several Google search results

import requests, webbrowser, bs4

print("Enter the string to search:")
search = input()

print('Googling........') # display text while performing search

res = requests.get('http://google.com/search?q=' + ' '.join(search))

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(1, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))