from django import forms
from .models import Customer, SavingsAccount, MFAccount, LoanAccount

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fName', 'lName', 'Aadhaar', 'Pincode']

class SavingsAccountForm(forms.ModelForm):
    class Meta:
        model = SavingsAccount
        fields = ['initial_amount']

class MFAccountForm(forms.ModelForm):
    class Meta:
        model = MFAccount
        fields = ['initial_investment']

class LoanAccountForm(forms.ModelForm):
    class Meta:
        model = LoanAccount
        fields = ['loan_amount']

class FigureForm(forms.Form):
    amount = forms.DecimalField(max_digits=11, decimal_places=2, min_value=1, max_value=99999999999)        