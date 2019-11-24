#!/usr/bin/env python
import grequests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from gamelogs import Gamelogs
from export import CSV
from gamelogsurls import GamelogUrls

year = None
is_valid = None
initial_url = 'https://www.sports-reference.com/cbb/seasons/2019-school-stats.html'


while year is None:
    input_value = input('Enter starting year: ')

    if(input_value.isdigit() and len(input_value)!= 4):
        print('{input} is not a valid year.'.format(input=input_value))
        continue
    else:
        try:
            year = int(input_value)
        except ValueError:
            print('{input} is not a number.'.format(input=input_value))
            continue
        else:
            is_valid = True
            break

print('fetching gamelogs since {} season... program will exit once complete'.format(year))

if(is_valid):
    urls = GamelogUrls(year, initial_url)

    url_has_data = True
    data = []
    counter=0
    

    request = (grequests.get(link) for link in urls.get_gamelogs_urls())
    response = grequests.imap(request)
    

    for link in response:
        
        if link:
            has_data = url_has_data
            new_url = link.url
            gamelogs = []
            counter = 0
            new_year = year
            while has_data:
                
                try:
                    next_url = new_url
                    initial_request = Request(next_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'})
                    page = urlopen(initial_request)
                    
                    raw_html = BeautifulSoup(page, 'html.parser')
                    
                    logs = Gamelogs(raw_html)
                    latest_gamelogs = logs.get_gamelogs_data()
                    heading = logs.get_heading()
                    
                    if counter==0:
                        gamelogs+=heading
                    gamelogs+=latest_gamelogs
                        
                    
                    new_year += 1
                    next_url = '/'.join((new_url.split('/')[:6]+[str(new_year)+'-gamelogs.html']))
                    new_url = next_url
                    counter += 1
                except:
                    has_data = False

            data.append(gamelogs)
        
    csv = CSV(data,year)
    csv.generate_csv()
