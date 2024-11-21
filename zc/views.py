from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
# def user(req):
    # user = User.objects.create_user(username='bingo',password='4321',email='bing2gmail.com')
    # user.save()
    # user = User.objects.get(username='bingo')
    # if user.check_password('4321'):
    #     return HttpResponse(f'user authenticated successfully ! username:{user.username}')
    # else:
    #     return HttpResponse('user not found!')
    # user =  User.objects.get(username='bingo')
    # user.is_staff=True
    # user.save()
    # return HttpResponse('bingo')

from .forms import custform
def cus(req):
    if req.method == 'POST':
        form =custform(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('x')
    else:
        form = custform()
    return render(req,'cusform.html',{'dat':form})

def vcus(req):
    data = customuser.objects.all()
    return render(req,'vcus.html',{'value':data})


def logins(req):
    if req.method == 'POST':
        username = req.POST.get('name')
        password = req.POST.get('password')
        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,'invalid username')
    return render(req,'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def home(req):
    return render(req,'home.html')

def log_out(req):
    logout(req)
    messages.info(req,'You have been logout')
    return redirect('x')


@login_required
def roll(req):
    if req.user.groups.filter(name='Manager').exists():
     return render(req,'rol.html')
    else:
        return HttpResponse('you do not have permission')



# @login_required
# def dashboard(request):
#     if request.user.groups.filter(name='admin').exists():
#         value="Admin"
#         return render(request,'admin_page.html',{'name':value})
#     elif request.user.groups.filter(name='staff').exists():
#         value="Staff"
#         return render(request,'admin_page.html',{'name':value})
#     elif request.user.groups.filter(name='customer').exists():
#         value="Customer"
#         return render(request,'admin_page.html',{'name':value})
#     else:
#         return HttpResponse("You do not have permission to this page")


