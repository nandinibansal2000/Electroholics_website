from django.urls import path , include
from .views import TableView


urlpatterns = [
    path('' , TableView.as_view() , name="table"),
]
