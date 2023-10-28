from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# ,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created, you can now LogIn {username}!')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    # if request.method == 'POST':
    #     u_form=UserUpdateForm(request.POST,instance=request.user)
    #     p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request,f'Your Account has been update, Thanks !')
    #         return redirect('profile')
    # else:
    #     u_form=UserUpdateForm(instance=request.user)
    #     p_form=ProfileUpdateForm(instance=request.user.profile)

        

    # context={
    #     'u_form':u_form,
    #     'p_form':p_form
    # }
    return render(request,'users/profile.html')


# from django.http import HttpResponse
# from django.shortcuts import render

# import twilio.rest

# def verify_phone_number(request):
#     client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#     phone_number = request.POST['phone_number']

#     verification = client.verify.services(TWILIO_VERIFY_SERVICE_SID).verifications.create(
#         to=phone_number,
#         channel='sms'
#     )

#     return render(request, 'verify_phone_number.html', {'verification_id': verification.sid})
