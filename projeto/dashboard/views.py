# dashboard/views.py


from django.shortcuts import render

def home(request):
    return render(request, "dashboard/dashboard.html", {})

def dashboard(request):
    return render(request, "dashboard/dashboard.html", {})
    pass

def add_expense(request):
    return render(request, "dashboard/add_expense.html", {})
    pass
#def login_view(request):
    # Sua lógica para a view de login aqui
 #   pass