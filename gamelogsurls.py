from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class GamelogUrls:
    def __init__(self, year, initial_url):
        self.year = year
        self.initial_url = initial_url


    def get_gamelogs_urls(self):
        request = Request(self.initial_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'})
        page = urlopen(request)
        raw = BeautifulSoup(page, 'html.parser')

        rows = raw.find('tbody', attrs={}).find_all('tr', recursive=False)

        current_year = self.year
        links=[]
        uri=[]
        schools_uri=[]
        gamelogs_urls=[]
            
        for row in rows:
            try:
                line = row.find('td', attrs={'data-stat':'school_name'}).find_all('a')
                links.append(line)
            except:
                pass

        for link in links:
            uri.append(link[0].get('href'))
            schools_uri.append(link[0].get('href').split('/')[3])


        for index, school in enumerate(schools_uri):
            url = 'https://www.sports-reference.com'+('/'.join(uri[index].split('/', 4)[:4]))+'/'+str(current_year)+'-gamelogs.html'
            gamelogs_urls.append(url)
        return gamelogs_urls