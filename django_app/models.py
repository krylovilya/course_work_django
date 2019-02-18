from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.contrib.auth.models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    CHOSE_GENDER = (
        ('man', 'Мужской'),
        ('woman', 'Женский')
    )
    email = models.EmailField(blank=False)
    #login = models.CharField(max_length=100, verbose_name="Логин", default="")
    #email = models.EmailField(verbose_name="Email", default="")
    #name = models.CharField(max_length=100, verbose_name="Имя")
    #surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=True)
    gender = models.CharField(max_length=10, choices= CHOSE_GENDER, default=CHOSE_GENDER[0], verbose_name="Пол")
    date_birth = models.DateField(auto_now=False, null=True, blank=True, verbose_name="Дата рождения")
    #date_reg = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")
    photo = models.URLField(max_length=100, verbose_name="Фото профиля", blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Pin(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(max_length=1000, blank=True, default="", verbose_name="Содержание")
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")
    #likes = models.ForeignKey(User, verbose_name="Лайки", on_delete=)
    photo = models.URLField(max_length=100, verbose_name="Изображение")

    def __str__(self):
        return "{}, {} {}".format(self.title, self.autor.first_name, self.autor.last_name)

    class Meta:
        verbose_name = "Пин"
        verbose_name_plural = "Пины"


class Like(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
