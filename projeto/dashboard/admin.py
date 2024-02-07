# dashboard/admin.py

from django.contrib import admin
from dashboard.models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)