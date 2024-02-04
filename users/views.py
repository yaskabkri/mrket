from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def u_hm(request):
    return render(request,'users/user.html')
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to user list page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usr')  # Redirect to user list page or any other page
    else:
        form = UserCreationForm(instance=user)
    return render(request, 'users/update_user.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Redirect to user list page or any other page
    return render(request, 'users/delete_user.html', {'user': user})


from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Specify your custom login template


class CustomLogoutView(LogoutView):
    pass




# views.py
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def update_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/update_profile.html', {'form': form})

# views.py
from django.shortcuts import render
from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})
