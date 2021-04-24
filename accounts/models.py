from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.






class auth_user(AbstractUser):
    about=models.TextField(blank=True,max_length=500)
    is_doctor=models.BooleanField(default=True,blank=False)
    doctor_type=models.CharField(max_length=64,default='MBBS')
    activation_code=models.CharField(default='null',max_length=11,blank=False)
    activation_code_provided=models.CharField(default='none',max_length=11,blank=True,unique=False)
    activated=models.BooleanField(default=False)
    



class Profile(models.Model):
    user=models.OneToOneField(auth_user,on_delete=models.CASCADE)
    Profile_pic=models.ImageField(upload_to='p_img',blank=True)
    
    def __str__(self):
        return self.user.username


class user_certification(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    title=models.CharField(max_length=64)
    text=models.CharField(max_length=500)
    certificate=models.ImageField(upload_to='p_img',blank=True)
   



    

