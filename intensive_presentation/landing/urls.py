from django.urls import path
from . import views

urlpatterns = [
    path("", views.myOwnView.as_view(), name="page"),
]