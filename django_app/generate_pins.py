import requests
import json
import random
from django_app.models import User, Pin


def do():
    count_users = User.objects.count()
    for i in range(90):
        pin = Pin()
        pin.autor = User.objects.all()[random.randint(0, count_users - 1)]
        r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png')
        json_r = json.loads(r.content)
        j = 0
        for x in range(10000):
            j += 1
        cat_url = json_r[0].get('url')
        cat_title = json_r[0].get('id')
        pin.photo = cat_url
        pin.title = "Кот №{}".format(cat_title)
        pin.text = "Привет, я {} и вот мой '{}' пин".format(pin.autor, cat_title)
        pin.save()
