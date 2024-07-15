
from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import Custdet

# Create your views here.

def home(request):
    return render(request,'webp1.html')


def custdet(request):

    if request.method =='POST':
        form=custform(request.POST)
    if forms.is_valid():
        return HttpResponseRedirect('/thanks/')
    else:
        form=Custdet()
    return render(request, 'webp2.html', {'form': form})

#def login(request):
    #return render (request, 'prac02.html')

