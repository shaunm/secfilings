#Created by NGT Apps

import re
from requests import get
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36', 'Connection': 'Keep-Alive'}

def getData(ticker):
    #Gets some data from the SEC and returns a dictionary
    url = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='+ticker+'&type=&dateb=&owner=exclude&count=40&output=atom'
    
    page = get(url, headers=headers).text
    soup = BeautifulSoup(page, "lxml")
    info = soup.find('company-info')
    if info == None:
        raise ValueError('You entered an invalid ticker.')

    
    cik = info.find('cik').text
    description =info.find('assigned-sic-desc').text
    name = info.find('conformed-name').text
    yrEnd = info.find('fiscal-year-end').text


    data = {"name":name.capitalize(), "cik":cik, "industry": description, "yrEnd":yrEnd, "ticker": ticker.upper()}
    return data


def getForm(ticker, name):
    #Gets a form from the SEC and returns as a dictionary
    name = name.upper()
    if not(name == "10-K" or name == "10-Q" or name == "8-K"):
        raise ValueError('You entered an invalid form.')
    
    cik = getData(ticker)['cik']
    url = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='+str(cik)+'&type='+name+'&dateb=&owner=exclude&count=40&output=atom'
    
    page = get(url, headers=headers).text
    soup = BeautifulSoup(page, "lxml")

    content = soup.find('entry').find('content')
    formType = content.find('filing-type').text
    dateFiled = content.find('filing-date').text
    followUrl = content.find('filing-href').text
    
    followContent = get(followUrl).content
    soup2 = BeautifulSoup(followContent , "lxml")
    fileLink = "https://www.sec.gov" + soup2.find_all('div', attrs={'id':'formDiv'})[1].find_all('a')[0]['href']

    data = {"form": formType, "date":dateFiled, "url":fileLink}
    return data


