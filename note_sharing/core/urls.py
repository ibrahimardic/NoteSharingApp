from django.urls import path
from . import views

urlpatterns = [
    # taking indexes from views.py file.
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup')
]
