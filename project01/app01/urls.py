"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home page'),
    path('register', views.register, name='register page'),
    path('student_reg', views.student_reg, name='student regis'),
    path('studentregister_details', views.studentregister_details, name='studentregister_details'),
    path('custdet', views.custdet, name='custdet'),
    path('test', views.test, name='test1'),
    path('user_details', views.user_details, name='userdetails'),
    #path('login', views.login, name='login'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact')
    
   


    
    
]
