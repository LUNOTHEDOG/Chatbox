from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import  SignUp

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')

    else:
        form = SignUp()

        return render(request, 'core/signup.html', {'form': form })
