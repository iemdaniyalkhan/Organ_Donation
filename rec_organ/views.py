from django.shortcuts import render,redirect
from django import template
from django.contrib.sessions.models import Session
import string
from datetime import date
import datetime
from datetime import datetime
import csv

import datetime
from datetime import date
import matplotlib.pyplot as plt


from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Avg, Max, Min, Sum, Count

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



from rec_organ.models import *
from blog.models import *
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import hashlib
from django.db.models import Q




def home(request):
    return render(request,'home.html',{})


def about(request):
    return render(request,"about.html",{})


def User_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        password = password.encode('utf-8')

        password = hashlib.new("md5",password).hexdigest()
        
        if user_Details.objects.filter(Username=Username, Password=password).exists():
                user = user_Details.objects.all().filter(Username=Username,Password=password)
                
                request.session['user_id'] = str(user[0].id)
                request.session['type_id'] = 'user'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                print(request.session['user_id'])
                messages.info(request,'valid Credentials')
                return redirect('/abc/')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/User_login/')
    else:
        return render(request, 'User_login.html', {})







def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
      
        
        if Admin_details.objects.filter(Username=Username, Password=password).exists():
                admin = Admin_details.objects.all().filter(Username=Username,Password=password)
                
                request.session['admin_id'] = str(admin[0].id)
                request.session['type_id'] = 'Admin'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                return redirect('/abc/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})

    



def Register(request):
    if request.method == 'POST':
        
        Username = request.POST['Username']
       
        Password = request.POST['Password']
        Password = Password.encode('utf-8')

        Password = hashlib.new("md5",Password).hexdigest()
        print(Password)
        Address =  request.POST['Address']
        State =  request.POST['State']
        City =  request.POST['City']
        CreditCard =  request.POST['CreditCard']
        MM =  request.POST['MM']
        YYYY =  request.POST['YYYY']

        CCExpiry = MM+"/"+YYYY
        Cvv =  request.POST['Cvv']


        Expiry_date = datetime.datetime.now() + datetime.timedelta(30)
        Expiry_date = Expiry_date.strftime('%Y-%m-%d')
        print(Expiry_date)

        if Admin_details.objects.filter(Username=Username).exists():
            messages.info(request,'Username taken')
            return redirect('/AddOfficer/')

       

        else:
            register1 = Admin_details(Username =Username,Password = Password)
            register1.save()

            messages.info(request,'Registration Done Successful')
            return redirect('/Register/')
    else:
        return render(request, 'register.html', {})





def adminreg(request):
    if request.method == 'POST':
        print("this one")
        U = request.POST['doc_name']
        abc = request.FILES['abc']
        abcd = request.FILES['abcd']
        P = request.POST['doc_qua']
        A = request.POST['adhar']
        print("heres the length")
        length = len(A)
        print(len(A))

        if user_Details.objects.filter(Username=U).exists():
            messages.info(request,'Username taken')
            return redirect('/adminreg/')

        elif length>12 or length<12:
            messages.info(request,'ADHAR NUMBER NOT CORRECT!')
            return redirect('/adminreg/')

        else:
        
            print(abcd)
            print("Starts")
        
            P = P.encode('utf-8')

            P = hashlib.new("md5",P).hexdigest()
            a = Post.objects.all().filter(title="by a")
            for x in a:
                print(type(x.file))


        
        
            
            register12 = user_Details( Username = U,Password = P,Adhar=A,Image1=abc,video=abcd)
            register12.save()
            users = user_Details.objects.all().filter(Username=U)
            print("this is the end one")
            for z in users:
                print(z.video)
                print(z.id)
                print(z.Username)
                print(z.Password)
                print(z.Adhar)
                print(z.Image1)

                
            abcd_video=z.video
            abcd_id = z.id
            abcd_username= z.Username
            abcd_password= z.Password
            abcd_adhar = z.Adhar
            abcd_image1 = str(z.Image1)
            


            register14 = Post(id =abcd_id,title=abcd_adhar,content=abcd_adhar,date_posted=0,file=abcd_video)
            register14.save()

            #Post.objects.filter(title="by a").update(file=abcd_video)
            #print("after process")
            a = Post.objects.all().filter(title=abcd)
            for y in a:
                print(y.file)




            messages.info(request,'Registered!')
            return redirect('/adminreg/')
    else:
        return render(request, 'adminreg.html', {})



def logout(request):
    if request.session['type_id'] == 'User':
        uid = request.session['User_id']
        Admin_details.objects.filter(id=uid).update(ChatStatus='Offline')
    
    Session.objects.all().delete()
    return redirect('/')


def ViewUsers(request):
    if request.method == 'POST':
        return redirect('/ViewUsers/')
    else:
        users = Admin_details.objects.all()
        print(users)
        return render(request, 'ViewUsers.html', {'users':users})























def api(request):
    #directory change
     print("api")
     return redirect('/E:/Postgre project/Postgre project/ecommerce rec_organ/movieapi/Templates/api.html/')
    
def admin_CP(request):
    if request.method == 'POST':
        CurrentPassword = request.POST['CurrentPassword']
        CurrentPassword = CurrentPassword.encode('utf-8')
        CurrentPassword = hashlib.new("md5",CurrentPassword).hexdigest()
        NewPassword = request.POST['NewPassword']
        NewPassword= NewPassword.encode('utf-8')
        NewPassword = hashlib.new("md5",NewPassword).hexdigest()
        ConfirmPassword = request.POST['ConfirmPassword']
        ConfirmPassword = ConfirmPassword.encode('utf-8')
        ConfirmPassword = hashlib.new("md5",ConfirmPassword).hexdigest()
        
        
        uid = request.session['admin_id']
        CurrUser = user_Details.objects.all().filter(id=uid)
        if CurrUser[0].Password == CurrentPassword:
            if NewPassword == ConfirmPassword:
                user_Details.objects.filter(id=uid).update(Password=NewPassword)
                messages.info(request,'Passwords Changed Successfully')
                return render(request, 'admin_CP.html', {})
            else:
                messages.info(request,'New Passwords doesnt match')
                return render(request, 'admin_CP.html', {})
        else:
            messages.info(request,'Current Password doesnt match')
            return render(request, 'admin_CP.html', {})
        
    else:
        return render(request, 'admin_CP.html', {})



#code starts here************************************************************************************************************************************************






def AcceptStylish(request):
    if request.method == 'POST':
        donername = request.POST['donor_name']
        donerage = request.POST['donor_age']
        donerbg = request.POST['donor_bg']
        print(donerbg)
        name = request.POST['name']
        location = request.POST['location']
        
        price = request.POST['price']        
        
        print(name)
        
        register3 = organ(donor_name=donername,donor_age=donerage,donor_BG=donerbg,name = name,location = location,price = price)
        register3.save()

        messages.info(request,'Product Successfully added')
        return redirect('/AcceptStylish/')
    else:
        return render(request, 'AcceptStylish.html', {})


def ViewSty(request):
    if request.method == 'POST':
        return redirect('/ViewSty/')
    else:

        itemz = organ.objects.all()
        return render(request, 'ViewSty.html', {'itemz':itemz})



def deluser(request,id):
    print(id)
    new = id
    
    
    d = organ.objects.all().filter(id = id)

    for x in d:
        print(x.name)

    
    
    
   
    
    organ.objects.filter(id=id).delete()
    messages.info(request,'organ deleted!')
    return redirect('/ViewSty/')





def updorg(request,id):
    print("started")
    itemz = organ.objects.filter(id=id)
    
    
    organs = organ.objects.all().filter(id=id)
                
    request.session['organs_id'] = str(organs[0].id)
    request.session['type_id'] = 'organs'

    
    print("yes")
    print(id)
    
    return render(request, 'AcceptStylishs.html', {'itemz':itemz})

def AcceptStylishs(request):
    

    if request.method == 'POST':
        
        print("this one")
        
        
        
        oid = (request.session['organs_id'])
        print("this one now")
        donorname = request.POST['donor_name']
        donerage = request.POST['donor_age']
        donerbg = request.POST['donor_bg']
        name = request.POST['name']
        location = request.POST['location']
        
        price = request.POST['price']
        print("new name")        
        
        print(name)
        print("starts the function here")
        organ.objects.filter(id=oid).update(donor_name=donorname,donor_age=donerage,donor_BG=donerbg,name=name,location=location,price=price)
        print("got updated")
        
    
        messages.info(request,'Product Successfully updated')
        return redirect('/ViewSty/')
    else:
        return render(request, 'AcceptStylishs.html', {})



def ViewStylish(request):
    if request.method == 'POST':
        return redirect('/ViewStylish/')
    else:
        itemz = organ.objects.all()
        return render(request, 'ViewStylish.html', {'itemz':itemz})


def searchs(request):
    template='ViewStylish.html'

    query=request.GET.get('q')

    result=organ.objects.filter(Q(donor_name__icontains=query) | Q(donor_age__icontains=query) | Q(donor_BG__icontains=query) | Q(name__icontains=query) | Q(location__icontains=query) | Q(price__icontains=query) | Q(stat__icontains=query))
    paginate_by=2
    context={ 'organ':result }
    return render(request,template,context)




def AcceptRequest(request,id):
    print(id)
    new = id
    print("accepted part starts")
    
    
    d = organ.objects.all().filter(id = id)

    for x in d:
        print(x.name)
        print(x.stat)

        prod_name = x.name

    organ.objects.filter(id=id).update(stat="booked")


    

    
    
    
   
    
    print("this")
    uid = request.session['user_id']
    print(uid)
    e = user_Details.objects.all().filter(id = uid)
    for y in e:
        print(y.Username)
        print(y.Image1)
        print(y.video)
        print(y.id)
        abc_ima= y.Image1
        abc_vi=y.video
        abc = y.Username

        
    print(abc)
    
    

    register8 = requests_made(names =abc,thing=prod_name,status="Pending",Image1=abc_ima,video=abc_vi,vid_id=uid)
    register8.save()
    f = requests_made.objects.all().filter(names = abc)
    for fs in f:
        print(fs.id)

    new_id = fs.id
    #Post.objects.filter(id=uid).update(id=uid)


    '''if Post.objects.filter(id=uid).exists():
         Post.objects.filter(id=uid).update(id=uid)'''


    
    
    
    
    
    messages.info(request,'Requested!')
    return redirect('/ViewStylish/')
          


def ViewStylis(request):
    if request.method == 'POST':
        return redirect('/ViewStylis/')
    else:
        uid = request.session['user_id']
        print("hello")
        print(uid)
        prod = user_Details.objects.all().filter(id=uid)
        for x in prod:
            named = x.Username

        print(named)

        prods = requests_made.objects.all().filter(names=named)
        
        return render(request, 'ViewStylis.html', {'prods':prods})

def accept(request,id):
    print(id)
    new = id
    requests_made.objects.filter(id=id).update(status="Accepted")
    
    
    messages.info(request,'Request Accepted!')
    return redirect('/View/')


def see_image(request,id):
    print("started")
    user_item = user_Details.objects.filter(id=id)
    
    
    usern = user_Details.objects.all().filter(id=id)
                
    request.session['usern_id'] = str(usern[0].id)
    request.session['type_id'] = 'usern'

    
    print("yes")
    print(id)
    a = user_Details.objects.all().filter(id=id)
    for x in a:
        print(x.Username)
    
    
    
    return render(request, 'see_image.html', {'user_item':user_item})


def reject(request,id):
    print(id)
    new = id
    requests_made.objects.filter(id=id).update(status="Rejected")
    
    
    messages.info(request,'Request Rejected!')
    return redirect('/View/')

def View(request):
    if request.method == 'POST':
        return redirect('/View/')
    else:

        a = organ.objects.all()
        itemz = requests_made.objects.all()
        return render(request, 'View.html', {'itemz':itemz,'a':a})
        
        
       
      

    
    























        

    









    
    








        














    



        




        

    












