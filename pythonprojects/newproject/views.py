from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(reqest):
    if reqest.method=='POST':
        username=reqest.POST['username']
        password=reqest.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(reqest,user)
            return redirect('/')
        else:
            messages.info(reqest,"Invalid credentials")
            return redirect('login')
    return render(reqest,"login.html")

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_Name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['password1']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                print("Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                print("Email already exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)

                user.save();
                return redirect('login')



        else:
          messages.info(request,"Password not matching.")
          return  redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')





