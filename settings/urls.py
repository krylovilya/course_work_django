from django.urls import path
from . import views
from . import views

urlpatterns = (
    path('', views.Index.as_view()),
    path('change_password/', views.ChangePassword.as_view()),
    path('change_email/', views.ChangeEmail.as_view()),
    path('change_photo/', views.ChangePhoto.as_view()),
)
