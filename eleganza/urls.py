from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my_profile', views.all_appointments, name='my_profile'),
    path('book', views.book, name='book'),
    path('edit/<appointment_id>/', views.edit_booking, name='edit'),
    path('cancel/<appointment_id>/', views.cancel_booking, name='cancel'),
]
