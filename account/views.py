from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentication successfully')
                
                else:
                    return HttpResponse('account disabled')
             
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})

#Login required 
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section':'dashboard'})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))