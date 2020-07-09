from django.contrib import admin
from django.urls import path , include
from .views import HelloApiView

urlpatterns = [
    path('', HelloApiView.as_view()),
    

]