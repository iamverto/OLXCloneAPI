# Generated by Django 3.1.12 on 2021-07-22 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='extra',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]