from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    url = 'https://newsapi.org/v2/everything?q=Cryptocurrency&from=2023-09-08&sortBy=popularity&apiKey=0d0bc652f2b5417290a89ef4616b8ae9'

    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]
    
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img)
    context = {'mylist': mylist}
    return render(request, 'index.html', context)