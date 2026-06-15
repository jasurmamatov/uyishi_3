from  django.urls import path
from .views import SignUp, LoginView, logoutview, ProfileView, ChangePasswordView, UserUpdateView


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logoutview , name='logout'),  
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-pass/', ChangePasswordView.as_view(), name='change-pass'),
    path('update/', UserUpdateView.as_view(), name='update'),
    
]