from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login(req):
    return render(req,'login.html')

    # if req.method=='POST':
    #     uname=req.POST['username']
    #     password=req.POST['password']
    #     data=authenticate(username=uname,password=password)
    #     if data:
    #         if data.is_superuser:
    #             login(req,data)
    #             req.session['admin']=uname
    #             return render(req,'home page/home.html')
    #         else:
    #             login(req,data)
    #             req.session['user']=uname
    #             return redirect()
    # else:
    #     return render(req,'login.html')

def d_home(req):
    return render(req,'home_page/home.html')
