#serializers
from .models import *
from rest_framework import serializers
#from django.contrib.auth import get_user_model

class ChawoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chawo
        fields = '__all__'
