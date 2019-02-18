# Generated by Django 2.1.3 on 2019-01-07 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0007_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Pin'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
