from profile import Profile

from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from .models import OwnerAdd, Vallet, Goods
from .serializers import ChawoSerializer, Chawo



class ChawoView(generics.ListAPIView):
    serializer_class = ChawoSerializer
    queryset = Chawo.objects.all()
class TestTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
       a = request.query_params
       queryset = Chawo.objects.all()
       a=Chawo.objects.filter(id=a['a'])
       return render(request,'index.html',{'posts':queryset,'answ':a})
       #Response({'profiles': queryset})

class LkTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lk.html'

    def get(self, request):
       a = request.query_params
       OA=OwnerAdd.objects.filter(owner=a['id'])
       VT=Vallet.objects.filter(owner=a['id'])
       GS=Goods.objects.filter(owner=a['id'])
       return render(request,'lk.html',{'user':OA[0],'wallet':VT[0],'goods':GS})
       #Response({'profiles': queryset})