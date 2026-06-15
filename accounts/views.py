from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm, LoginForm, ChangePasswordForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from products.utils import trigger_email_view, trigger_email_view_login


# Create your views here.
class SignUp(View):
    def get(self, request):
        form = UserForm(request.POST)
        
        return render(request , 'accounts/signup.html', context = {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
        
        return render(request, 'accounts/signup.html', context = {'form': form})
        
        
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        # phone_number = request.POST.get('phone_number')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        
        
        # user = CustomUser(first_name=first_name, last_name = last_name, username = username, phone_number = phone_number, email = email, password = password)
        # user.set_password(password)
        # user.save()
        
        # CustomUser.objects.create_user(first_name=first_name, last_name = last_name, username = username, phone_number = phone_number, email = email, password = password)
        
        
        # return redirect('home')



def home(request):
    return render(request, 'home.html')






class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
          
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

@login_required
def logoutview(request):
    logout(request)
    return redirect("home")



class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/profile.html') 
    

class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'accounts/change_pass.html', {'form': form})
    
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            
            user = authenticate(username = request.user.username, password=old_password)
            if not user:
                raise ValidationError('eski parol xato')
            
            user.set_password(new_password)
            user.save()
            
            return redirect('profile')
        
        return render(request, 'accounts/change_pass.html', {'form': form})

            
            
class UserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, 'accounts/update.html', {'form': form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'accounts/update.html', {'form': form})