from django.urls import path
from . import views

urlpatterns = (
    #path('', views.Index.as_view()),
    path('<pin_id>', views.LikeView.as_view()),
)
