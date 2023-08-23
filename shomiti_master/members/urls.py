from django.urls import path

from .views import login_page, logout_page, dashboard, newmembers, members_list, new_employee, employee_list
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import hotel_image_view

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),

    # branch
    path('newmembers/', newmembers, name='newmembers'),
    path('members-list/', members_list, name='members_list'),
    path('new-empoyee/', new_employee, name='new_employee'),
    path('employee-list/', employee_list, name='employee_list'),
    path('', dashboard, name='dashboard'),

    # dps
    path('add-dps/', views.add_dps, name='add_dps'),
    path('dps-collections/', views.dps_collections, name='dps_collections'),
    path('dps-list/', views.dps_list, name='dps_list'),
    path('dps-opening-report/', views.dps_opening_report,
         name='dps_opening_report'),
    path('dps-schemes/', views.dps_schemes, name='dps_schemes'),
    path('dps-withdraw-report/', views.dps_withdraw_report,
         name='dps-withdraw-report'),

    # expenses
    path('add-expenses/', views.add_expenses, name='add_expenses'),
    path('category-expenses/', views.category_expenses, name='category_expenses'),
    path('expenses-list/', views.expenses_list, name='expenses_list'),

    # accounts
    path('accounts/', views.accounts, name='accounts'),

    # fdr
    path('add-fdr/', views.add_fdr, name='add_fdr'),
    path('fdr-list/', views.fdr_list, name='fdr_list'),
    path('fdr-opening-report/', views.fdr_opening_report,
         name='fdr_opening_report'),
    path('fdr-schemes/', views.fdr_schemes, name='fdr_schemes'),
    path('fdr-withdraw-report/', views.fdr_withdraw_report,
         name='fdr_withdraw_report'),

    # loan
    path('loan-collect/', views.loan_collect, name='loan_collect'),
    path('loan-fine/', views.loan_fine, name='loan_fine'),
    path('loan-ledger/', views.loan_ledger, name='loan_ledger'),
    path('loan-list/', views.loan_list, name='loan_list'),

    # report
    path('collection-report/', views.collection_report, name='collection_report'),
    path('expense-report/', views.expense_report, name='expense_report'),
    path('fine-report/', views.fine_report, name='fine_report'),
    path('loan-report/', views.loan_report, name='loan_report'),
    path('report-by-employee/', views.report_by_employee,
         name='report_by_employee'),
    path('report-by-member/', views.report_by_member, name='report_by_member'),
    path('summery-report/', views.summery_report, name='summery_report'),

    path('image_upload/', hotel_image_view, name='image_upload'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
