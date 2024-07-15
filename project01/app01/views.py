from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
#from .models import Card, Anish, Student, NewStudent, StudentRegister, OtherRegister


# Create your views here.


def home(request):

    # stud=Student.objects.all().order_by("id")
    # newstud=NewStudent.objects.all().order_by("id")
    # std=StudentRegister.objects.all()
    # oth=OtherRegister.objects.all()

    # context={
    #     'stud': stud,
    #     'std': std,
    #     'oth': oth,
    #     'newstud': newstud

    # }



    
    '''
    card1=Card()

    card1.id=''
    card1.name="Dog"
    card1.img='dog.png'
    '''
    #return render(request, 'stud.html', context)
    #return render(request,'test1.html')
    #return render(request, "studentform.html")
    #return render(request, "sampleformpage.html")
    #return render(request, "sampleformhome.html")
    return render(request, "studentclass_home.html")


def studentregister_details(request):

    std=StudentRegister()
    std.name=request.POST["name"]
    std.sex=request.POST["sex"]
    std.phone=int(request.POST["phone"])
    std.email=request.POST["email"]
    std.dob=request.POST["dob"]
    std.father_name=request.POST["father_name"]
    std.username=request.POST["username"]
    std.password1=request.POST["password1"]
    std.password2=request.POST["password2"]
    std.secretq=request.POST["secretq"]
    std.secreta=request.POST["secreta"]
    
    context = {

            "formname": std.name, 
            "formsex" : std.sex,
            "formphone": std.phone, 
            "formemail": std.email,
            "formdob": std.dob, 
            "formusername": std.username,
            "formfathername" : std.father_name,
            "formsecretq": std.secretq,
            "formsecreta": std.secreta

    }

    return render(request, 'student_registrationdetails.html',  context)


def otherregister_details(request):

    oth=OtherRegister()
    oth.name=request.POST["name"]
    oth.sex=request.POST["sex"]
    oth.phone=int(request.POST["phone"])
    oth.email=request.POST["email"]
    oth.dob=request.POST["dob"]
    oth.father_name=request.POST["father_name"]
    oth.username=request.POST["username"]
    oth.password=request.POST["password"]
    oth.secretq=request.POST["secretq"]

    context = {

            "formname": oth.name, 
            "formsex" : oth.sex,
            "formphone": oth.phone, 
            "formemail": oth.email,
            "formdob": oth.dob, 
            "formfathername" : oth.father_name,
            "formsecretq": oth.secretq

    }

    return render(request, 'result.html',  context)


def register(request):
    return render(request, "user_register.html")

def student_reg(request):
    return render(request, "student_registration.html")

def about(request):
    return render(request, "studentclass_about.html")

def contact(request):
    return render(request, "studentclass_contact.html")

def login(request):
    return render(request,'userlogin.html')

def user_details(request):
    user1=Anish() 
    user1.name=request.POST["name"]
    user1.sex=request.POST["sex"]
    user1.phone=int(request.POST["phone"])
    user1.email=request.POST["email"]
    
    context = {

            "formname": user1.name, 
            "formsex" : user1.sex,
            "formphone": user1.phone, 
            "formemail": user1.email

    }

    return render(request, 'result.html',  context)
   

def test(request):    
    #return render(request, 'test1.html')
    a=int(request.GET["num1"])
    b=int(request.GET["num2"])
    c=a+b
    
    return render(request,'test1.html', {"sum": c})

def custdet(request):

    ackn=request.user
    name=request.GET["cust_name"]
    fname=request.GET["fath_name"]
    date=request.GET["dob"]
    #curaddr=request.GET["curaddr"]
    #mobile=int(request.GET["mob_no"])


    
    form = {
        'Acknowledgement No.': ackn,
        'Applicant Name': name,
        'Father Name':  fname,
        'Date of Birth': date,
    
    }
    
    return render(request, 'webp2.html', {'form': form})

def login(request):
    return render (request, 'prac02.html')

