
from django.urls import path
from core import views

urlpatterns = [
    path('', views.login_view, name='login'),
]
