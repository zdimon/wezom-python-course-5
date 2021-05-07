from django.forms import ModelForm
from account.models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['fullname', 'username', 'password', 'phone' ]

