import requests
from bs4 import BeautifulSoup
from pprint import pp
from .models import BotData

import pandas as pd

# get the data
def get(url):
    """
    its a funtion to get the data from webpage
    """    
    page = requests.get(url) 
    if page.status_code == 200:
        htmldata = page.text
        soup = BeautifulSoup(htmldata, 'lxml')
        print('success')
        return soup
    else:
        print('error',page.status_code)

def extract(soup, query):
    page_products = [] # will hold the products from a page
    titles = soup.find_all('div',attrs={'class':'_4rR01T'})
    prices= soup.find_all('div',attrs={'class':'_30jeq3 _1_WHN1'})
    links = soup.find_all('a', attrs={'class':'_1fQZEK'})

    for t,p,a in zip(titles,prices,links):
        data = {
            'title' : t.text,
            'price' : p.text,
            'link':a.attrs.get('href'),
            'category':query,
        }
        b = BotData(title=t.text, price=p.text, url=a.attrs.get('href'), category=query)
        b.save()
        page_products.append(data)
    print('total product collected',len(page_products))
    return page_products


if __name__ == "__main__":

    url = "https://www.flipkart.com/search?"
    search_term = "laptop"
    page = 1
    filename = 'laptop_23dec.csv'

    scraped_products = [] 
    while True:
        starturl = f"{url}q={search_term}&page={page}"
        print('getting data from',starturl,'...')
        soup = get(starturl)
        if not soup:
            print('scraper closed')
            break
        else:
            output = extract(soup)
            if len(output) == 0:
                print('scraper closed')
                break
            scraped_products.extend(output)
            print('total size of collected data', len(scraped_products))
            page += 1

    # save the stuff
    save(scraped_products,filename)