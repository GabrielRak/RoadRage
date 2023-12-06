from django.urls import path
from . import views

urlpatterns  = [
    path('', view=views.home),
    path('sign_up', view=views.sign_up)
]
