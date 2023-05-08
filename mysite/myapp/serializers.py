#serializers
from django.contrib.auth import get_user_model

from .models import *
from rest_framework import serializers
#from django.contrib.auth import get_user_model

class ChawoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chawo
        fields = '__all__'
class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        #fields =     "Name","cost","image","sold_type","IS_3D","IS_2D","IS_AUDIO"
        exclude=['owner']
class ValletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vallet
        exclude = ['owner','money']
        #fields = 'web','money','vallet_number'
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerAdd
        exclude = ['owner','mark']
        #fields = 'mark','img_res'


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )


