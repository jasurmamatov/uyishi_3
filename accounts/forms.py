from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
        
        
    def clean(self):
        cleaned_data = super().clean()
            
            
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password  and password != confirm_password:
            raise ValidationError("Parollar mos emas")
        return cleaned_data
        
       
                   
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and len(username) < 8:
            raise ValidationError("Username 8 tadan kichik bo'lmasin")
        return username
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        
        if len(last_name) < 10:
            raise ValidationError("Last_name 10 tadan kichik bo'lmasin")
        return last_name
    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        
        if "@gmail.com" not in email:
            raise ValidationError("Email noto'g'ri kiritildi ")
        return email
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        
        if len(phone_number) != 7:
            raise ValidationError("phone_number 7 raqamdan iborat bolishi kerak")
        return phone_number
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get("password")
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        
      
        return username
            
        
        
    
    
