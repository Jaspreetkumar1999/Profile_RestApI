from django.contrib import admin
from django.urls import path , include
from .views import HelloApiView , HelloViewSet, UserProfileViewSet,LoginViewSet,UserProfileFeedViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename = 'hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, basename='login')
router.register('feed', UserProfileFeedViewSet)




urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('',include(router.urls)),
    

]