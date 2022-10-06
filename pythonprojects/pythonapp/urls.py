from . import views
from django.urls import path
urlpatterns = [

    path('',views.home,name='home'),

    path('demo1/', views.addition, name='addition')





    # path('about/',views.about,name='about'),
   # path('contact/',views.contact,name='contact'),
   # path('details',views.details,name='details'),
   # path('thank',views.thank,name='thank'),
]
