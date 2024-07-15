from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .import forms

def register(request):
    if request.method == 'POST':
        reg_form = forms.RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect("homepage")

    else:
        reg_form = forms.RegistrationForm()
    return render(request,"register.html",{'form':reg_form})

class Login(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return  super().form_invalid(form)

class user_logout(LogoutView):
    def get(self,request):
        logout(request)
        return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("homepage")

    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request,"edit_profile.html",{'form':profile_form})

def profile(request):
    return render(request,'profile.html')
    

