from bs4 import BeautifulSoup as bs

import requests

url = 'https://github.com/' + input ("Enter the github username: ")
req = requests.get (url)

soup = bs (req.text, 'html.parser')

if soup.title != None:
    print(soup.find_all ('h2', {'class': 'f4 text-normal mb-2'})[0].next)
    repo = requests.get (url + '?tab=repositories').text
    repoSoup = bs (repo, 'html.parser')

    if repoSoup.find('div', {'class': 'pagination' }) != None:
        pageTotal = repoSoup.find('div', {'class': 'pagination' }).find_all('a')
    else:
        pageTotal = []
    lastPage = 0 if len(pageTotal) == 0 else pageTotal[len(pageTotal) - 2].next


    if (len(pageTotal) > 0):
        for idx in range(1, int(lastPage) + 1):
            page = requests.get (url + '?page=' + str(idx) + '&tab=repositories')
            pageSoup = bs (page.text, 'html.parser')
            for h3 in pageSoup.find_all('h3'):
                print(h3.next.next.get('href'))
    else:
        for h3 in repoSoup.find_all('h3'):
            print(h3.next.next.get('href'))
else:
    print ('Username not found')    
