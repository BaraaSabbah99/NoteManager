from django.shortcuts import render ,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password ,check_password
from django.db.models import Q

# Create your views here.


def registeration(request):

    if request.method == 'POST':
     try:
      user = User.objects.get(Q(username=request.POST.get('username')) | Q(email=request.POST.get('email')))
     except:
        user = None
     if user != None:
           return redirect('users:register')
     else:
           username=request.POST.get('username')
           email=request.POST.get('email')
           password = make_password(request.POST.get('password'))
           user = User(username=username,email=email,password=password)
           user.save()
           return redirect('index')
    else:
        return render(request,'register.html')
    


def login(request):
    
    if request.method == 'POST':
       try:
           user = User.objects.get(username=request.POST.get('username'))
       except:
           user = None
       if user == None:
           return redirect('users:login')
       else:
           password = request.POST.get('password')
           checker = check_password(password,user.password)
           if checker:
               request.session['id'] = user.id 
               request.session['role'] = user.role
               return redirect('index')
           else:
               return redirect('users:login')
    else:
        return render(request,'login.html')




def logout(request):
    request.session.flush()
    return redirect('users:login')



def dashbored(request):
    try:
        role = request.session['role']
    except:
        role = None

    if role == None or role == 'user':
        return redirect('users:login')
    else:
        users = User.objects.filter(role ='user')
        return render(request,'admin.html',{"users":users})



def search(request):
    if  request.method == 'GET' and request.GET.get('search') == 'search':
        try:
            user = User.objects.get(username=request.GET.get('name'))
        except:
            user = None
        
        if user == None:
            return render(request,'notfound.html')
        else:
            return render(request,'usersearch.html',{"usersearch":user})
    else :
        return HttpResponse("Error")
        


def deleteuser(request,userId):

    try:
        user = User.objects.get(id=userId)
    except:
        user = None
    
    if user == None:
        return redirect('users:admin')
    
    else:
        user.delete()
        return redirect('users:admin')