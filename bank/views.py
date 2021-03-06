from django.shortcuts import render
from bank.models import User,Transfer
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime


def index(request):
    if request.method=="POST":
        username=request.POST.get("user")
        url = '{}{}'.format('transfer/', username)
        return redirect(url)
    
    
    user=User.objects.all()
    us={
        "user":user
        }
    return render(request,'index.html',us)


def Home(request):
    return render(request,'Home.html')

def Registeration(request):
    if request.method=="POST":
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        balance=request.POST.get('balance')
        password=request.POST.get('password')
        user=User(Username=username,name=name,email=email,balance=int(balance) ,password=password)
        user.save()
    return render(request,'Registeration.html')



def transfer(request,username):
    user=User.objects.filter(Username=username)
    u={
       "user":user,
       "hh":"0"
       }
    
    if request.method=="POST":
        to=request.POST.get("to")
        From=username
        amount=request.POST.get("amount")
        date=datetime.datetime.now()
        u["hh"]="1"
        
        for i in user:
            i.balance=i.balance-int(amount)
        
        
        user2=User.objects.filter(Username=to)
        for j in user2:
            j.balance=j.balance+int(amount)
        
        
        transfer=Transfer(To=to,From=From,amount=amount,date=date)
        i.save()
        j.save()
        transfer.save()
    
    
    return render(request,'transfer.html',u)