import csv

from django.http import HttpResponse
from .models import Account, TransactionDetail
from .serializers import AccountSerializers, DepositSerializer, MoneyWithdrawSerializers, CreateAccountSerializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .IsOwner import IsOwner

# Create your views here.


class CreateAccount(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializers


class AccountEnquiry(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    lookup_field = 'accNo'


class MoneyDeposit(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = DepositSerializer
    lookup_field = 'accNo'
    permission_classes = [IsAuthenticated]


class MoneyWithdraw(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner, IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = MoneyWithdrawSerializers
    lookup_field = 'accNo'


def export_transactions_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Transaction On', 'Deposit By', 'Deposit', 'Withdraw', 'Account No'])

    transactions = TransactionDetail.objects.all().values_list('transactionOn', 'depositBy', 'deposit', 'withdraw', 'accountNo')
    for transaction in transactions:
        writer.writerow(transaction)

    return response