from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.core.mail import send_mail
import random,string


from .models import auth_user 
from .models import Profile,user_certification
from django.conf import settings


import time
# Create your views here.




#explains what to do when user fill registeration form and hit submit
def registerAccount(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if (password1==password2):
            if auth_user.objects.filter(username=username,activated=True).exists():
                print("Username Taken")
                messages.info(request,'user name taken')
                messages.info(request,'Enter Valid credential')
                
                return render(request,"registerAccount.html")
            elif auth_user.objects.filter(email=email,activated=True).exists():
                
                print("Email Taken")
                messages.info(request,'Email taken')
                messages.info(request,'Please Enter Valid Credential')
                return render(request,"registerAccount.html")
            elif len(password1)<8:
                messages.info(request,'password must be at least 8 charactors')

            else:

                
                codelist=[]
                letters = string.ascii_lowercase
                for i in range(11):
                    randomnum=random.choice(letters)
                    codelist.append(randomnum)

                b=''.join(codelist)
                while auth_user.objects.filter(activation_code=b).exists()==True:
                    codelist=[]
                    letters = string.ascii_lowercase
                    for i in range(11):

                        randomnum=random.choice(letters)
                        codelist.append(randomnum)

                    b=''.join(codelist)




                print(b)
                auth_user.objects.filter(username=username).delete()
                auth_user.objects.filter(email=email).delete()
                user=auth_user.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email,activation_code=b)
                
                user.save()



                send_mail(
                'Activate your Account',
                'Please Enter the Following Code to Activate your Account: '+b,
                'bellachao8611@gmail.com',
                [user.email],
                fail_silently=False,
                                    )
                userx=auth.authenticate(username=username,password=password1)
                auth.login(request,userx)




                print("userCreated")
          
                time.sleep(2)
                return redirect('activate')
                
        else:
            print("Password Doesn't Match")
            messages.info(request,'Password Does not match')
            return render(request,"registerAccount.html")
        
        return render(request,'registerAccount.html',{"first_name":first_name})

    else:
        return render(request,"registerAccount.html")


#explains what to do when user fill login form and hit submit
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Invalid credentials ')
            print('first if')
            return render(request,'loginpagestylish.html')
        else:

            


            auth.login(request,user)
            print('2nd else')
            if user.activated==True:

                return redirect('profile',user.username)
            else:
                return redirect('activate')

           

        return redirect('profile',user.username)
            
    
    else:

        return render(request,'loginpagestylish.html',)

def changeprofilepic(request):   
    if request.method=='POST' or request.method=='FILES':
        print(request.user.id)
        profile_pic=request.FILES['image']
        if Profile.objects.filter(user_id=request.user.id).exists():
            Profile.objects.filter(user_id=request.user.id).delete()
            p=Profile(Profile_pic=profile_pic,user_id=request.user.id)
            p.save()
            messages.info(request,'Profile Pic Updated Successfully')
            return render(request,'profile_pic_change.html')

        else:
            p=Profile(Profile_pic=profile_pic,user_id=request.user.id)
            p.save()
            messages.info(request,'Updated Successfully')
            return render(request,'profile_pic_change.html')

        return render(request,'profile_pic_change.html')

    else:
        return render(request,'profile_pic_change.html')



def activateaccount(request):
    if request.method=='POST':
        code=request.POST['activationcode']
        x=auth_user.objects.get(email=request.user.email)
        if x.activation_code==code:
            auth_user.objects.filter(email=request.user.email).update(activation_code_provided=code,activated=True)
            return redirect('profile',request.user.username)
        else:
            messages.info(request,'Invalid Code')
            return render(request,'activate.html')
            
        
        #When user login. i'll send him to activate/ link and will add conidition here .

        return render(request,'activate.html')
    else:
        return render(request,'activate.html')






#explains what to do when user is logged in .
def profile(request,user_name):
    if request.method=='POST':

        
    
        if user_name==request.user.username:
            
            certs=user_certification.objects.filter(user_id=request.user.id).all()
            
            
            
        
            return render(request,'profile.html',{'certs':certs})
        else:
            return redirect('profile')
        return render(request,'profile.html',{'certs':certs})
    else:

        if user_name==request.user.username:


            certs=user_certification.objects.filter(user_id=request.user.id).all()

            return render(request,'profile.html',{'certs':certs})
        else:


            if request.user.is_authenticated and request.user.activated==True and auth_user.objects.filter(username=user_name).exists():
                ot_auth_user=auth_user.objects.get(username=user_name)
                
                

                first_name=ot_auth_user.first_name
                last_name=ot_auth_user.last_name
                email=ot_auth_user.email
                username=ot_auth_user.username
                is_doctor=ot_auth_user.is_doctor
                about=ot_auth_user.about
                
                doctor_type=ot_auth_user.doctor_type
                user_id=ot_auth_user.id
                
                if Profile.objects.filter(user_id=ot_auth_user.id).exists():
                    ot_profile=Profile.objects.get(user_id=ot_auth_user.id)
                    p_pic=ot_profile.Profile_pic
                    

                    return render(request,'othersprofile.html',{
                        'first_name':first_name,
                        'last_name':last_name,
                        'email': email,
                        'username':username,
                        'is_doctor':is_doctor,
                        'about':about,
                        'is_doctor':is_doctor,
                        'doctor_type':doctor_type,
                        'user_id':user_id,
                        'profile_pic':p_pic,
                                                  })                
                else:
                    print('doesnt exist')
                   
                return render(request,'othersprofile.html',{
                    'first_name':first_name,
                    'last_name':last_name,
                    'username':username,
                    'is_doctor':is_doctor,
                    'about':about,
                    'email': email,
                    'doctor_type':doctor_type,
                    'user_id':user_id,
                    
                    
                        })

            else:
                if request.user.is_authenticated==True and auth_user.objects.filter(username=user_name).exists()==False:
                    return HttpResponse('invalid link')
                else:
                    if request.user.is_authenticated==True:

                        return render(request,'loginhelpactivate.html')
                    else:
                        return render(request,'loginhelpnologon.html')

def appointment(request,user_name):
    if request.method=='POST':
        text=request.POST['text']

        return render(request,'appointment.html',{'text':text})
    else:
        return redirect('profile',user_name)
           
       

    
    

   
#logouts
def logout(request):
    auth.logout(request)
    return redirect('/')


#what to do when user hit profile settings.
def profilesettings(request):   
    if request.method=='POST' or request.method=='FILES':

        
        about=request.POST['about']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        doctortype=request.POST['doctortype']

        a=auth_user.objects.filter(username=request.user.username).update(first_name=first_name,last_name=last_name,doctor_type=doctortype,about=about)
        messages.info(request,'Updated Successfully')
        return render(request,'profilesettings.html')
    else:
        return render(request,'profilesettings.html')
        
        

    




def certificationsetting(request):
    if request.method=='POST' or request.method=='FILES':
        title=request.POST['title']
        text=request.POST['text']
        c1=request.FILES['image']
        cert=user_certification(certificate=c1,text=text,title=title,user_id=request.user.id)
        cert.save()
        messages.info(request,'Updated Successfully')

        return render(request,'certificationsettings.html')

    else:

        

        return render(request,'certificationsettings.html')



def deletecertificate(request):
    if request.method=='POST':
        a=request.POST['pkid']
        
        user_certification.objects.filter(user_id=request.user.id,id=a).delete()
        return redirect('profile',request.user.username)
    else:
        return redirect('profile',request.user.username)







    







