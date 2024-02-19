from django.urls import path
from .views import dashboard, add_expense, get_expense_data, dashboard2, dashboard3, graficos

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_expense/', add_expense, name='add_expense'),
    path('dashboard2/', dashboard2, name='dashboard2'),
    path('dashboard3/', dashboard3, name='dashboard3'),
    path('api/expenses/', get_expense_data, name='get_expense_data'),
]