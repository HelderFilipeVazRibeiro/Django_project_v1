# dashboard/admin.py

from django.contrib import admin
from dashboard.models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'amount', 'description')  # Campos exibidos na lista de visualização
    list_filter = ('category',)  # Filtros laterais com base na categoria
    search_fields = ('description',)  # Campo de pesquisa para descrição
    #pass
    def get_expense_data(self):
        expenses = self.get_queryset().values('date', 'amount')
        return expenses

admin.site.register(Expense, ExpenseAdmin)
