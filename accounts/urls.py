from  django.urls import path
from .views import SignUp, LoginView, logoutview


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logoutview , name='logout')    
    
    
]