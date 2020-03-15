
from . import views
from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   path('count/',views.count, name='count'),
   path('aboutpage/',views.aboutpage,name='about'),
  
]
