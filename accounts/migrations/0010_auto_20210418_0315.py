# Generated by Django 3.1.7 on 2021-04-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210417_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='auth_user',
            name='activation_code_provided',
            field=models.CharField(default='null', max_length=11, unique=True),
        ),
    ]
