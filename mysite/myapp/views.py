from profile import Profile

from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from .models import OwnerAdd, Vallet, Goods
from .serializers import ChawoSerializer, Chawo



class ChawoView(generics.ListAPIView):
    serializer_class = ChawoSerializer
    queryset = Chawo.objects.all()

class AllView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mainmenu.html'


class TestTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
       a = request.query_params
       if a:
           pass
       else: a= {'a':1}
       queryset = Chawo.objects.all()
       a=Chawo.objects.filter(id=a['a'])
       return render(request,'index.html',{'posts':queryset,'answ':a})
       #Response({'profiles': queryset})

class LkTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = 'lk.html'
    def get(self, request):
       a = request.user
       print(request.COOKIES.get("acces"))
       OA=OwnerAdd.objects.filter(owner=a)
       VT=Vallet.objects.filter(owner=a)
       GS=Goods.objects.filter(owner=a)
       return render(request,'lk.html',{'user':OA[0],'wallet':VT[0],'goods':GS})
       #Response({'profiles': queryset})
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        response.set_cookie("acces", token, httponly=True)
        return response