from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django_app.models import User, Pin, Like
from django.views.generic import TemplateView


class Index(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(request.user.username)
        else:
            return HttpResponseRedirect("/")


class ViewId(TemplateView):
    def get(self, request, *args, **kwargs):
        user = User.objects.filter(username=kwargs['username']).first()
        if not user:
            return HttpResponseRedirect("/")
        pins = Pin.objects.filter(autor=user)
        likes = {}
        for pin in pins:
            likes.update({pin.id: Like.objects.filter(pin=pin).count()})
        context = {"username": user.get_username(),
                   "user_id": user.id,
                   "user": user,
                   "likes": likes,
                   "all_pins": pins,
                   }

        return render(request, "user.html", context)
