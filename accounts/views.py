from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm
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