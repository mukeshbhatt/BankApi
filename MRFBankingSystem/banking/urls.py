from django.urls import path
from .views import MoneyWithdraw, AccountEnquiry, MoneyDeposit,CreateAccount, export_transactions_csv

urlpatterns = [
    path('createAccount/', CreateAccount.as_view(), name='create-retrieve account'),
    path('retrieveAccount/<int:accNo>/', AccountEnquiry.as_view(), name='retrieve account'),
    path('deposit/<int:accNo>/', MoneyDeposit.as_view(), name='Money-Deposit'),
    path('withdraw/<int:accNo>/', MoneyWithdraw.as_view(), name='Money-Withdraw'),
    path('exportCsv/', export_transactions_csv, name='export_transaction_csv'),
]