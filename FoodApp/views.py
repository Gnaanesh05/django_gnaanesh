from django.shortcuts import render,redirect
from .models import Food,Consume_Food
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def IndexPage(request):
    return render(request,'Index.html')
def loadLogin(request):
    return render (request,'loadAdminlogin.html')

def adminlogin(request):
    if request.method=='POST':  
         
        vuname=request.POST.get('uname')
        vpasswd=request.POST.get('passwd')
        newuser=auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request,newuser)
            messages.success(request,'Successfully logged in !!!')
            return redirect('/home')
        else:
            messages.success(request,"Kindly login again!!")
            return redirect('/loadLogin')

def Home(request):
    if request.method =='POST':
        consumed_food=request.POST.get('food_consumed')
        consume=Food.objects.get(name=consumed_food)
        user=request.user
        consume=Consume_Food(user=user,food_consumed=consume)
        consume.save()
        food=Food.objects.all()
    else:
        food=Food.objects.all()
    consumed_food=Consume_Food.objects.filter(user=request.user)
    return render(request, 'Homepage.html', {'food': food,'consume_food':consumed_food})

def delFoodConsume(request,fid):
    consume_food=Consume_Food.objects.get(id=fid)
    consume_food.delete()
    return redirect('/home')
