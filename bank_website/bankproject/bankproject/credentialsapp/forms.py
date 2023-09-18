from django import forms
from .models import District, Branch, Account


class AccountForm(forms.ModelForm):
    DEBIT_CARD = 'DC'
    CREDIT_CARD = 'CC'
    CHEQUE_BOOK = 'CB'

    MATERIAL_CHOICES = [
        (DEBIT_CARD, 'Debit Card'),
        (CREDIT_CARD, 'Credit Card'),
        (CHEQUE_BOOK, 'Cheque Book'),
    ]

    materials = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MATERIAL_CHOICES,
    )
    class Meta:
        model = Account
        fields = '__all__'
