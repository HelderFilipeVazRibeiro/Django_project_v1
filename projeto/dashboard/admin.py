# dashboard/admin.py

from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'amount', 'description')  
    list_filter = ('category',)  # <----- filtros laterais, das categorias que existem
    search_fields = ('description',)  # campo de pesquisa para descricao
    #pass
    def get_expense_data(self):
        expenses = self.get_queryset().values('date', 'amount')
        return expenses

admin.site.register(Expense, ExpenseAdmin)
