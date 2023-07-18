from django.urls import path
from . import views 
from .views import ContextView, IndexView

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('list/', ContextView.as_view(), name='list'),
] 