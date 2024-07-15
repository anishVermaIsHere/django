from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth

#from .models import Card, Anish, Student, NewStudent, StudentRegister, OtherRegister


#from .forms import NameForm
# Create your views here.


def loginform(request):
    return render(request, "sampleformlogin.html")

def login(request):

    if request.method=="POST":    
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("useraccount")
        else:
            messages.info(request,'Account does not exist! Enter correct username')
            return redirect('loginform')
    else:
        return render(request,"sampleformlogin.html")



def useraccount(request):
    return render(request, "useraccount.html")

def editprofile(request):
    return render(request, "user_editprofile.html")


def logout(request):

    auth.logout(request)
    return redirect('loginform')


'''
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'current_name': form})

'''

    