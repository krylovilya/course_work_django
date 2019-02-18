from django.urls import path
from . import views
from . import views

urlpatterns = (
    path('', views.Index.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('register/validate_email', views.ValidateEmail.as_view()),
    path('get_pin/', views.GetPin.as_view()),
    path('gpins/', views.Gpins.as_view()),
    path('add_pin/', views.AddPinView.as_view()),
)
