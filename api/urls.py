
from django.urls import path
from .views import Index,PersonList,PersonDetails

urlpatterns = [
    path('index/',Index),
    path('persons/',PersonList.as_view()),
    path('persons/<int:id>/',PersonDetails.as_view())
]