# Generated by Django 3.1.7 on 2021-04-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210418_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='auth_user',
            name='activation_code',
            field=models.CharField(default='null', max_length=11),
        ),
        migrations.AddField(
            model_name='auth_user',
            name='activation_code_provided',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
