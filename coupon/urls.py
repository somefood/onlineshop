from django.urls import path
from . import views

app_name = 'coupon'
urlpatterns = [
    path('add/', views.add_coupon, name='add'),
]