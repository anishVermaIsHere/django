from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth

#from .models import Card, Anish, Student, NewStudent, StudentRegister, OtherRegister


#from .forms import NameForm
# Create your views here.


def home(request):
    a = request.user
    e = "anish@python.com"

    context = {
        'username': a,
        'email': e,
        'array_city': [ "Delhi", "Bengaluru", "Mumbai" ]
    
    }

   
    #return render(request,'name3.html', context)
    return render(request, "sampleformhome.html")

 # for register form

def register(request):

    if request.method=="POST":    
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]


    if password1==password1:
        if User.objects.filter(username=username).exists():
            print("Username is already exist");
        elif User.objects.filter(email=email).exists():
            print("Email is already used");
        else:
            user=User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password2)
            user.save();
            print("Registration is done successfully");
        return redirect("registersuccess")
    else:

        return render(request, "sampleformregister.html")



def registersuccess(request):
    return render(request, "registersuccessfully.html")
    
def registerform(request):
    return render(request, "sampleformregister.html")

def contact(request):
    return render(request, "sampleformcontact.html")

def aboutus(request):
    return render(request, "sampleformabout.html")

def services(request):
    return render(request, "sampleformservices.html")


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

    