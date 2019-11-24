from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from gamelogsurls import GamelogUrls

class Gamelogs:
    def __init__(self, raw_html):
        self.raw_html = raw_html
        
    
    def get_gamelogs_data(self):
        try:
            rows = self.raw_html.find('tbody', attrs={}).find_all('tr', recursive=True)
                
            gamelogs_raw = []
            gamelogs=[]

            for row in rows:
                try:
                    gamelogs_raw.append(row.find_all('td'))
                except:
                    pass

            for gamelog in gamelogs_raw:
                data = []
                for logs in gamelog:
                    data.append(logs.string)
                if data:
                    gamelogs.append(data)       
            return gamelogs
        except:
            return None
        
        
    def get_gamelogs_headers(self):
        rows = self.raw_html.find('thead', attrs={}).find_all('tr', recursive=True)[1]
        headers_raw=[]
        headers_list=[]
        
        
        for row in rows:
            headers_raw.append(row)
        
        for header in headers_raw:
            if(header.string!='\n'):
                headers_list.append(header.string)
        
        headers = [headers_list[1:]]
        
        return headers

    def get_school_name(self):
        rows = self.raw_html.find('div', attrs={'id':'info'}).find_all('span', recursive=True)

        school_name = []
        school_name.append([rows[1].string])

        return school_name


    def get_heading(self):
        headers = self.get_gamelogs_headers()
        school = self.get_school_name()
        
        gamelogs = school+headers
        
        return gamelogs
        
        