from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('hello/', views.index, name='index'),
    path('login/', views.loginpage, name='index'),

]
