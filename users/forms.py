from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import phonenumbers
from phonenumbers import is_valid_number
from django.core.validators import RegexValidator
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    

    phone_regex = RegexValidator(
        regex=r'^\+91\d{10}$',
        message="Phone number must be entered in the format: '+919999999999'. Exactly 10 digits allowed after the country code."
    )
    
    phone = forms.CharField(validators=[phone_regex], max_length=13)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name','last_name','phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            parsed_phone = phonenumbers.parse(phone, 'IN')  # 'IN' is the country code for India
            if not is_valid_number(parsed_phone):
                raise forms.ValidationError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberFormatException:
            raise forms.ValidationError("Invalid phone number")

        return phone
    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=False)
    #     user.profile.phone = self.cleaned_data["phone"]  # Assuming you have a profile model with a 'phone' field
    #     if commit:
    #         user.save()
    #     return user
    
   

