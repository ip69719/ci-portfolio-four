from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my_profile', views.all_appointments, name='my_profile'),
    path('book', views.book, name='book'),
]
