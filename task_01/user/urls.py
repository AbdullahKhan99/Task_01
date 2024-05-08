from . import views
from django.urls import path

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('signin/',views.SignInView.as_view(),name="signin")
    
]
