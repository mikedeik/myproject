
from django.urls import path ,include
from .views import Index,PersonList,PersonDetails , UserList ,UserDetails , CategoryList , CategoryHandle, BidderList
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('',Index),
    path('persons/',PersonList.as_view()),
    path('persons/<int:id>/',PersonDetails.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:id>/',UserDetails.as_view()),

    path('category/',CategoryList.as_view()),
    path('category/<int:CategoryId>',CategoryHandle.as_view()),

    path('Bidders/' ,BidderList.as_view())


]