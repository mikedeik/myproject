
from django.urls import path
from .views import Index,person_list

urlpatterns = [
    path('index/',Index),
    path('persons/',person_list)
]