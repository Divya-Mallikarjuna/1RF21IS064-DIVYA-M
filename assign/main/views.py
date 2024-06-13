from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CustomerRegistrationForm, SavingsAccountForm, MFAccountForm, LoanAccountForm
from .models import Customer, SavingsAccount, MFAccount, LoanAccount
from django.urls import reverse
from django.utils.http import urlencode
from .forms import FigureForm
from num2words import num2words
from datetime import date


# icic account
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('products_page', customer_id=customer.CustomerId)
    else:
        form = CustomerRegistrationForm()
    return render(request, 'index.html', {'form': form})

def products_page(request, customer_id):
    return render(request, 'products.html', {'customer_id': customer_id})

def open_savings_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST)
        if form.is_valid():
            savings_account = form.save(commit=False)
            savings_account.customer = customer
            savings_account.save()
            return HttpResponse(f"Savings Account created successfully! Account Number: {savings_account.account_number}")
    else:
        form = SavingsAccountForm()
    return render(request, 'open_save.html', {'form': form, 'customer_id': customer_id})

def open_mf_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = MFAccountForm(request.POST)
        if form.is_valid():
            mf_account = form.save(commit=False)
            mf_account.customer = customer
            mf_account.save()
            return HttpResponse(f"MF Account created successfully! Account Number: {mf_account.account_number}")
    else:
        form = MFAccountForm()
    return render(request, 'open_mf.html', {'form': form, 'customer_id': customer_id})

def open_loan_account(request, customer_id):
    customer = get_object_or_404(Customer, CustomerId=customer_id)
    if request.method == 'POST':
        form = LoanAccountForm(request.POST)
        if form.is_valid():
            loan_account = form.save(commit=False)
            loan_account.customer = customer
            loan_account.save()
            return HttpResponse(f"Loan Account created successfully! Account Number: {loan_account.account_number}")
    else:
        form = LoanAccountForm()
    return render(request, 'open.html', {'form': form, 'customer_id': customer_id})

# cheque

def convert_figures_to_words(amount):
    return num2words(amount, lang='en_IN').title()  # Convert to words and capitalize each word

def convert_figure(request):
    if request.method == 'POST':
        form = FigureForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            words = convert_figures_to_words(amount)
            query_string = urlencode({'amount': amount, 'words': words})
            return redirect(f'{reverse("print_cheque")}?{query_string}')
    else:
        form = FigureForm()
    return render(request, 'c.html', {'form': form})

def print_cheque(request):
    amount = request.GET.get('amount')
    words = request.GET.get('words')
    context = {'amount': amount, 'words': words}
    return render(request, 'cheque.html', context)

# Encode

def encode_message(request):
    message = "Attack submarine near Karachi"
    encoded_message = encode(message)
    return HttpResponse(encoded_message, content_type="text/plain")

def encode(message):
    # Get today's date
    today = date.today()
    is_even_day = today.day % 2 == 0

    def encode_char(c):
        if c.isalpha():
            if is_even_day:
                # Encode for even day
                return str(500 + ord(c.upper()) - ord('A') + 1)
            else:
                # Encode for odd day
                return str(ord(c.upper()) - ord('A') + 1).zfill(2)
        # Return non-alphabet characters as is
        return c

    # Encode each character in the message
    encoded_chars = [encode_char(c) for c in message]
    # Join the encoded characters with spaces
    return ' '.join(encoded_chars)