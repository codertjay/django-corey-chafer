from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('blog_home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# do you know why @login_required it is because if the user just add profile to
# the url he would be directed to login so no scam like
@login_required
def profile(request):
    # the reasons why i am putting instance in my form is because i want the form to contain it username and all is
    # profile already so if the user wants to change its he would know what is going on and you know that the p_form
    # contain many things that is why p_form = ProfileUpdateForm(request.POST,request.FILES,
    # instance=request.user.profile) so you have to put everything in the tuple
    # and note you must check if the form is valid
    # and i put a success message for them to know that their account have being updated
    # and i redirect them to profile
    # to prevent the resubmission

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
