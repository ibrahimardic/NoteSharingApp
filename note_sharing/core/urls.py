from django.urls import path
from . import views

urlpatterns = [
    # taking indexes from views.py file.
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
