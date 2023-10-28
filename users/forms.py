from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from twilio.rest import Client
import phonenumbers
import random
from .models import CustomUser
from django.conf import settings

class UserRegistrationForm(UserCreationForm):
    phone_regex = RegexValidator(
        regex=r'^\+91\d{10}$',
        message="Phone number must be entered in the format: '+919999999999'. Exactly 10 digits allowed after the country code."
    )

    phone = forms.CharField(validators=[phone_regex], max_length=13)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            parsed_phone = phonenumbers.parse(phone, 'IN')
            if not phonenumbers.is_valid_number(parsed_phone):
                raise forms.ValidationError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberFormatException:
            raise forms.ValidationError("Invalid phone number")

        return phone

    def send_otp(self):
        account_sid ='ACa6fb482bd0864f78db4d8e16d7790e9e'
        auth_token = '17044712ae4d3e60d91072e94dea15f7'
        client = Client(account_sid, auth_token)

        otp = random.randint(1000,9999)# Generate a random OTP here

        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_='+12295751324',
            to=self.cleaned_data['phone']
        )
        print(otp)
        return otp
