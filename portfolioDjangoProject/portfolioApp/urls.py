from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('resume',views.resume),
    path('work',views.work),
    path('life',views.life),	   
]