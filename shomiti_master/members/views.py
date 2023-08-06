from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from .forms import EmployeeGranterLoginForm
from .models import Granter, Employee, Product
from django.contrib.auth.models import User
from .forms import EmployeeForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
   
    return render(request, 'dashboard.html')

#branch
@login_required(login_url='login')
def newmembers(request):
   
    return render(request, 'branch/newmembers.html')

@login_required(login_url='login')
def members_list(request):
   
    return render(request, 'branch/members-list.html')


#employee

@login_required(login_url='login')
def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
           
            return redirect('/members') 
            print(form.cleaned_data)  # Redirect to a success page
    else:
        form = EmployeeForm()
        print("error") 
    return render(request, 'branch/new-employee.html', {'form': form})


@login_required(login_url='login')
def employee_list(request):
    employees = Employee.objects.all()
    # granters = Granter.objects.all()
    
    # employee_list = {
    #     'employees': employees,
    #     'granters': granters
    # }
    
    return render(request, 'branch/employee-list.html', {'employees': employees})
   
#dps start

@login_required(login_url='login')
def add_dps(request):
   
    return render(request, 'dps/add-dps.html')

@login_required(login_url='login')
def dps_collections(request):
   
    return render(request, 'dps/dps-collection.html')

@login_required(login_url='login')
def dps_list(request):
   
    return render(request, 'dps/dps-list.html')

@login_required(login_url='login')
def dps_opening_report(request):
   
    return render(request, 'dps/dps-opening-report.html')

@login_required(login_url='login')
def dps_schemes(request):
   
    return render(request, 'dps/dps-schemes.html')
@login_required(login_url='login')
def dps_withdraw_report(request):
   
    return render(request, 'dps/dps-withdraw-report.html')

#expenses start
@login_required(login_url='login')
def add_expenses(request):
   
    return render(request, 'expenses/add-expenses.html')

@login_required(login_url='login')
def category_expenses(request):
   
    return render(request, 'expenses/category-expenses.html')

@login_required(login_url='login')
def expenses_list(request):
   
    return render(request, 'expenses/expenses-list.html')

#fdr start
@login_required(login_url='login')
def add_fdr(request):
   
    return render(request, 'fdr/add-fdr.html')

@login_required(login_url='login')
def fdr_list(request):
   
    return render(request, 'fdr/fdr-list.html')

@login_required(login_url='login')
def fdr_opening_report(request):
   
    return render(request, 'fdr/fdr-opening-report.html')

@login_required(login_url='login')
def fdr_schemes(request):
   
    return render(request, 'fdr/fdr-schemes.html')

@login_required(login_url='login')
def fdr_withdraw_report(request):
   
    return render(request, 'fdr/fdr-withdraw-report.html')

#loan start

@login_required(login_url='login')
def loan_collect(request):
   
    return render(request, 'loan/loan-collect.html')


@login_required(login_url='login')
def loan_fine(request):
   
    return render(request, 'loan/loan-fine.html')


@login_required(login_url='login')
def loan_ledger(request):
   
    return render(request, 'loan/loan-ledger.html')


@login_required(login_url='login')
def loan_list(request):
   
    return render(request, 'loan/loan-list.html')

#report


@login_required(login_url='login')
def collection_report(request):
   
    return render(request, 'report/collection-report.html')


@login_required(login_url='login')
def expense_report(request):
   
    return render(request, 'report/expense-report.html')


@login_required(login_url='login')
def fine_report(request):
   
    return render(request, 'report/fine-report.html')


@login_required(login_url='login')
def loan_report(request):
   
    return render(request, 'report/loan-report.html')

@login_required(login_url='login')
def report_by_employee(request):
   
    return render(request, 'report/report-by-employee.html')

@login_required(login_url='login')
def report_by_member(request):
   
    return render(request, 'report/report-by-member.html')


@login_required(login_url='login')
def summery_report(request):
   
    return render(request, 'report/summery-reports.html')

@login_required(login_url='login')
def accounts(request):
   
    return render(request, 'accounts/accounts.html')

def employee_granter_list(request):
    p = Product.objects.all()
    # granters = Granter.objects.all()
    
    # employee_info = {
    #     'employees': employees,
    #     'granters': granters
    # }
    
    return render(request, 'branch/employee-list.html', {'p':p})