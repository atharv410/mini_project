from django.shortcuts import render
from .models import BotData
from . import crawler as mpc
from django.contrib import messages
from django.http import HttpResponse
import csv

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['id','title','price','url', 'category','created_at'])

    records = BotData.objects.all().values_list('id','title','price','url', 'category','created_at')
    for row in records:
        writer.writerow(row)

    return response

def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)

def collect_data(request):
    ctx = {}
    if request.method=='POST':
        query= request.POST.get('query')
        if len(query) > 0:
            url = "https://www.flipkart.com/search?"
            search_term = query
            page = 1
            scraped_products = [] 
            while True:
                starturl = f"{url}q={search_term}&page={page}"
                print('getting data from',starturl,'...')
                soup = mpc.get(starturl)
                if not soup:
                    print('1.scraper closed')
                    break
                else:
                    output = mpc.extract(soup,query)
                    if len(output) == 0:
                        print('2.scraper closed')
                        break
                    scraped_products.extend(output)
                    print(f'total size of collected data {len(scraped_products)}')
                    page += 1
                if page == 10:
                    print('limit broken')
                    break
                if page == 1 and len(scraped_products):
                    print("Could not get data, try another query")
        else:
            messages.error("No query provided")
    return render(request, 'results.html', ctx)

def view_data(request):
    dataset = BotData.objects.all()
    ctx = {'dataset':dataset,}
    return render(request, 'viewdata.html', ctx)