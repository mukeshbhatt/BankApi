from rest_framework import serializers
from .models import Account, TransactionDetail


class AccountSerializers(serializers.ModelSerializer):
    username = serializers.StringRelatedField(many=False)

    class Meta:
        model = Account
        fields = ['username', 'accNo', 'balance', 'birth_date', 'account_open']


class CreateAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        exclude = ('deposit', 'withdraw')


class DepositSerializer(serializers.ModelSerializer):
    deposit = serializers.DecimalField(max_digits=7, decimal_places=2, max_value=1000000, min_value=1)

    class Meta:
        model = Account
        fields = ['deposit']

    def update(self, instance, validated_data):
        instance.accNo = validated_data.get('accNo', instance.accNo)
        instance.account_open = validated_data.get('account_open', instance.account_open)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        deposit = validated_data.get('deposit')
        current_balance = instance.balance
        instance.balance = (current_balance + deposit)
        instance.save()
        TransactionDetail.objects.create(depositBy=self.context['request'].user, deposit=deposit, accountNo=instance.accNo)
        return instance


class MoneyWithdrawSerializers(serializers.ModelSerializer):
    withdraw = serializers.DecimalField(max_digits=6, decimal_places=2, max_value=100000, min_value=1)

    class Meta:
        model = Account
        fields = ['withdraw']

    def update(self, instance, validated_data):
        instance.accNo = validated_data.get('accNo', instance.accNo)
        instance.account_open = validated_data.get('account_open', instance.account_open)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        withdraw = validated_data.get('withdraw')
        current_balance = instance.balance
        instance.balance = (current_balance - withdraw)
        instance.save()
        TransactionDetail.objects.create(depositBy=self.context['request'].user, withdraw=withdraw, accountNo=instance.accNo)
        return instance

