from django.urls import path
from . import views 

#Home
urlpatterns = [
    path('', views.home, name='home')

]
