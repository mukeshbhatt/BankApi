from django.core.mail import EmailMessage
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Account(models.Model):
    accNo = models.PositiveIntegerField(blank=False, unique=True)
    username = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    birth_date = models.DateField(null=True, blank=True)
    account_open = models.DateField(null=True, blank=True)
    deposit = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    withdraw = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.username


class TransactionDetail(models.Model):
    transactionOn = models.DateTimeField(default=timezone.now())
    depositBy = models.TextField(max_length=300)
    deposit = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    withdraw = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    accountNo = models.PositiveIntegerField()


@receiver(post_save, sender=Account)
def send_email(**kwargs):
    email = EmailMessage(
        'Summery', 'your transaction is successfully',
        'mukeshbhatt18@gmail.com',
        ['mukeshbhatt18@gmail.com']
    )
    email.send()
