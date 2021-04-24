from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Profile,auth_user


urlpatterns = [
    path('', views.home,name='home'),
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