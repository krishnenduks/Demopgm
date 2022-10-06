from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Food

# Create your views here.
def home(request):
   # name='india'
    obj=Place.objects.all()
    obj1=Food.objects.all()
    return  render(request,"index.html",{'result':obj,'results':obj1})

#def about(request):
    #return HttpResponse("Here you will get to know....")
#def contact(request):
   # return HttpResponse("Hloo my contact no is 456788235")
#def details(request):
   # return render(request, 'details.html')
#def thank(request):
   # return HttpResponse("Thank You..... ")


def addition(request):
   x=int(request.GET['num1'])
   y=int(request.GET['num2'])
   res=x+y
   res1=x-y
   res2=x*y
   res3=x/y

   return render(request,"result.html",{'result':res,'sub':res1,'mul':res2,'div':res3})



