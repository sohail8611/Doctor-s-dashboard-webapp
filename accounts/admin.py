from django.contrib import admin

# Register your models here.
from .models import auth_user,Profile


admin.site.register(Profile)
admin.site.register(auth_user)
