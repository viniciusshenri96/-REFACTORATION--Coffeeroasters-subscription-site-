from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('auth/', include('social_django.urls', namespace='social')), 
]
