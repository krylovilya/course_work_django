from django.contrib import admin
from . import models


#admin.site.register(models.User)


class UserAdmmin(admin.ModelAdmin):
    list_display = [field.name for field in models.User._meta.fields]
    search_fields = [field.name for field in models.User._meta.fields]

    class Meta:
        model = models.User


class PinAdmmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Pin._meta.fields]
    search_fields = [field.name for field in models.Pin._meta.fields]

    class Meta:
        model = models.Pin


class LikeAdmmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Like._meta.fields]
    search_fields = [field.name for field in models.Like._meta.fields]

    class Meta:
        model = models.Like


admin.site.register(models.User, UserAdmmin)
admin.site.register(models.Pin, PinAdmmin)
admin.site.register(models.Like, LikeAdmmin)
