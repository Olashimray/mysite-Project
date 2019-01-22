"""from django.shortcuts import render  
  
# Create your views here.  
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
"""
"""
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello Good to see you here')

def eggs(request):
    return HttpResponse('Eggs are great')
"""
from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request, 'home.html') #{'hithere':'this is me'})
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word]=1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)        

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':worddictionary.items})


def about(request):
    return render(request, 'about.html')
)
