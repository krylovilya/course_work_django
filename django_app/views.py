from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from . import forms, generate_pins
from .models import User, Pin, Like
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .render_pin import render_pin


class Gpins(TemplateView):
    def get(self, request):
        generate_pins.do()
        return redirect("/")


class Index(TemplateView):
    def get(self, request):
        if request.GET.get('pagination'):
            pagination = int(request.GET['pagination'])
        else:
            pagination = 1
        if request.GET.get('msg'):
            msg = request.GET['msg']
        else:
            msg = None
        add_pin_form = None
        if request.user.is_authenticated:
            add_pin_form = forms.AddPinForm()
        pins = Pin.objects.all().order_by('-id')[30 * (pagination - 1):30 * pagination]
        max_pagination = Pin.objects.count()
        if (Pin.objects.count() / 30).is_integer():
            max_pagination = Pin.objects.count() / 30
        else:
            max_pagination = Pin.objects.count() // 30 + 1

        likes = {}
        for pin in pins:
            likes.update({pin.id: Like.objects.filter(pin=pin).count()})
        print(likes)
        context = {
            "all_pin": pins,
            "likes": likes,
            "pagination": pagination,
            "msg": msg,
            "max_pagination": max_pagination,
            "add_pin_form": add_pin_form,
        }
        return render(request, "index.html", context)


class RegisterFormView(FormView):
    form_class = forms._UserCreationForm
    success_url = "/login"
    template_name = "register.html"

    def form_valid(self, form):
        if User.objects.filter(email=form.cleaned_data.get("email")):
            return super(RegisterFormView, self).form_invalid(form)
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect("/")


class ValidateEmail(TemplateView):
    def get(self, request):
        email = request.GET.get("email")
        if User.objects.filter(email=email).exists():
            data = {
                "is_taken": "На этот почтовый ящик уже зарегестрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"ok": "Всё окейсики)"})


class GetPin(TemplateView):
    def get(self, request):
        pin_id = request.GET.get("pin_id")
        if Pin.objects.filter(id=pin_id).exists():
            data = {
                "ok": "ok",
                "html": render_pin(Pin.objects.filter(id=pin_id).first())
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "Всё окейсики)"})


class AddPinView(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def post(self, request):
        form = forms.AddPinForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            pin = Pin()
            pin.autor = request.user
            pin.photo = form['photo'].value()
            pin.title = form['title'].value()
            pin.text = form['text'].value()
            pin.save()
            return redirect('/?msg=Пин добавлен')
        else:
            return redirect('/?msg=Форма некорректна')
