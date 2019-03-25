from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistionFroms

def registion(request):
    if request.method == 'POST':
        form = UserRegistionFroms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Sucess Fully {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistionFroms()
    return render(request, 'users/register.html', {'form': form})


