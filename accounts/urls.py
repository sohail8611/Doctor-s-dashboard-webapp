from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Profile,auth_user
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


  




urlpatterns = [
    path('', views.home,name='home'),
    path('api/accounts', views.auth_user_list.as_view(),name='home'),
    path('api/certifications', views.user_certification_list.as_view(),name='home'),
    path('api/profiles', views.Profile_list.as_view(),name='home'),
    path('accounts/register',views.registerAccount,name='registerAccount'),
    
    
    path('profile/<str:user_name>',views.profile,name='profile'),
   
    path('profile/accounts/logout',views.logout,name='logout'),
    path('profile/settings/',views.profilesettings,name='settings'),
    path('profile/settings/certification/',views.certificationsetting,name='csettings'),
    path('profile/deletecertificate/',views.deletecertificate,name='csettings'),
    path('profile/<str:user_name>/get_appointment',views.appointment,name='appointment'),
    path('activate',views.activateaccount,name='activate'),
    path('changeprofilepic',views.changeprofilepic,name='edit'),
    
    
  
   
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
