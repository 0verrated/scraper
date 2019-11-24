from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


class Schools:
    def __init__(self, url):
        self.url = url

    def getSchools(self):
        url = self.url
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'})
        page = urlopen(request)
        raw = BeautifulSoup(page, 'html.parser')

        rows = raw.find('tbody', attrs={}).find_all('tr', recursive=False)
        links=[]

        for row in rows:
            try:
                line = row.find('td', attrs={'data-stat':'school_name'}).find_all('a')[0].string
                links.append(line)
            except:
                pass
        return links
    
