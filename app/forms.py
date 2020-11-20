from django import forms

from app.models import Transaction


class TransactionForm(forms.ModelForm):
    bill_for = forms.CharField(label="Bill For", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    issue_date = forms.DateField(label="Issue Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    due_date = forms.DateField(label="Due Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    total = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    class Meta:
        model = Transaction
        fields = ['bill_for', 'issue_date', 'due_date', 'total', 'status']
