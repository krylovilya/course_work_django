from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_app import models
from .models import User


class _UserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ("username", "email")
        model = User


class AddPinForm(forms.Form):
    title = forms.CharField(max_length=200, label="Заголовок")
    text = forms.CharField(widget=forms.Textarea, max_length=1000, label="Текст", required=False)
    photo = forms.URLField(max_length=200, label="Ссылка на фото")
