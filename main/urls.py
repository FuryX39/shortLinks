from django.urls import path
from .views import index, redirect_to_full


urlpatterns = [
    path('', index, name='Home'),
    path('<str:short_id>/', redirect_to_full)
]
