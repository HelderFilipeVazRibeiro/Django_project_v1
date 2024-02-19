# dashboard/views.py


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator


def home(request):
    return render(request, "dashboard/dashboard.html", {})


def dashboard(request):
    expenses = Expense.objects.all()
    allowed_categories = Expense.ALLOWED_CATEGORIES 
    return render(request, 'dashboard/dashboard.html', {'expenses': expenses, 'allowed_categories': allowed_categories})

def add_expense(request):
    if request.method == 'POST':
        return redirect('dashboard')  # Redirecionar para a página de dashboard após o envio do formulário
    else:
        allowed_categories = Expense.ALLOWED_CATEGORIES  # Certifique-se de substituir 'Expense' pelo nome do seu modelo
        expenses = Expense.objects.all()  # Se necessário para renderizar a tabela de despesas
        return render(request, 'dashboard/add_expense.html', {'allowed_categories': allowed_categories, 'expenses': expenses})

def dashboard2(request):
    return render(request, "dashboard/dashboard2.html", {})
    

def dashboard3(request):
    return render(request, "dashboard/dashboard3.html", {})

def graficos(request):
    return render(request, "dashboard/graficos.html", {})

def get_expense_data(request):
    filter_value = request.GET.get('filter')

    if filter_value == 'day':
        expenses = Expense.objects.all()
    elif filter_value == 'month':
        expenses = Expense.objects.annotate(month=ExtractMonth('date')).values('month').annotate(total_amount=Sum('amount'))
    elif filter_value == 'year':
        expenses = Expense.objects.annotate(year=ExtractYear('date')).values('year').annotate(total_amount=Sum('amount'))

    data = list(expenses)
    return JsonResponse(data, safe=False)

#def dashboard_view(request):
 #   expenses = Expense.objects.all()
  #  return render(request, 'dashboard.html', {'expenses': expenses})

@require_POST
def add_expense(request):
    date = request.POST.get('date')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    description = request.POST.get('description')
    
    # Criar uma nova despesa e salvar no banco de dados
    Expense.objects.create(date=date, category=category, amount=amount, description=description)
    
    return redirect('dashboard')

