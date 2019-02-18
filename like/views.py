import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django_app.models import Like, Pin, User


class LikeView(LoginRequiredMixin, TemplateView):
    raise_exception = True

    def get(self, request, pin_id):
        pin = Pin.objects.get(id=int(pin_id))
        user = User.objects.get(username=request.user)
        is_like = bool(Like.objects.filter(pin=pin, user=user).count())
        print("\n\n\n" + pin_id + "\n\n\n")
        if is_like:
            Like.objects.filter(pin=pin, user=user).delete()
            result = "remove"
        else:
            new_like = Like()
            new_like.pin = pin
            new_like.user = user
            new_like.save()
            result = "add"
        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": Like.objects.filter(pin=pin).count(),
            }),
            content_type="application/json"
        )

    def post(self, request):
        raise Http404
