# login/urls.py


from django.urls import path
from django.views.generic import RedirectView
from login import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login')),  # Redireciona a rota padrão para a página de login
    path('login/', views.login_view, name='login'),
 
]