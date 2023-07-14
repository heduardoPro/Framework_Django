from django.urls import path
from . import views 

app_name = 'home'

#Home
urlpatterns = [
    path('', views.home, name='home'),
]
