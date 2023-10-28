from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# ,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from twilio.rest import Client

from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now log in as {username}!')

            # Send OTP to the user's phone number
            otp = form.send_otp()
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            print(otp)

            return redirect('otp_verification')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

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

def otp_verification(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        otp_entered = request.POST.get('otp')


        if user_id:
            # Initialize Twilio client
            client = Client('ACa6fb482bd0864f78db4d8e16d7790e9e', '17044712ae4d3e60d91072e94dea15f7')

            # Verify the OTP using Twilio
            verification = client.verify \
                .services('VAadc86ba4a22cc1806cff7c99add9e5cf') \
                .verification_checks \
                .create(to='+12295751324', code=otp_entered)


        
            if verification.status == 'approved':
                # OTP verification successful
                user = CustomUser.objects.get(id=user_id)
                messages.success(request, f'OTP verification successful. Your account has been created, you can now log in as {user.username}!')
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'users/otp_verification.html')
