from rest_framework import serializers
from . models import auth_user
from . models import user_certification,Profile
class auth_userSerializer(serializers.ModelSerializer):
    class Meta:
        model=auth_user
        fields='__all__'

class user_certificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_certification
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

