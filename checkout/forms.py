from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    # Range needs to be to 13 because Python drops the last number in the range
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(label="Card number (no spaces)", required=False)
    cvv = forms.CharField(label="Security code (CVV)", required=False)
    expiry_month = forms.ChoiceField(label="Expiry month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Expiry year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            "full_name",
            "house_number",
            "address1",
            "address2",
            "city",
            "county",
            "post_code",
            "country",
            "phone_number",
        )
