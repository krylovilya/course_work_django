from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import ChangeEmailForm, ChangePhotoForm
from django.views.generic import TemplateView
from django_app.models import User
from django.http import Http404


class Index(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def get(self, request):
        context = {}
        return render(request, "settings.html", context)


class ChangePassword(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('change_password')
        else:
            form = PasswordChangeForm(request.user)
            return render(request, 'change_password.html', {
                'form': form
            })

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form
        })


class ChangeEmail(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def get(self, request):
        #data = {'email': request.user.objects}
        form = ChangeEmailForm()
        return render(request, 'change_email.html', {
            'form': form
        })

    def post(self, request):
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            user.email = form['email'].value()
            user.save(update_fields=["email"])
            #request.user.save({'email': form['email']})
            return redirect('/settings/')
        else:
            return render(request, 'change_email.html', {
                'form': form
            })


class ChangePhoto(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def get(self, request):
        form = ChangePhotoForm()
        return render(request, 'change_photo.html', {
            'form': form
        })

    def post(self, request):
        form = ChangePhotoForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            user.photo = form['photo'].value()
            user.save(update_fields=["photo"])
            return redirect('/settings/')
        else:
            return render(request, 'change_photo.html', {
                'form': form
            })
