from profile import Profile

from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import ChawoSerializer, Chawo



class ChawoView(generics.ListAPIView):
    serializer_class = ChawoSerializer
    queryset = Chawo.objects.all()

class TestTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
       queryset = Chawo.objects.all()
       return render(request,'test.html',{'posts':queryset})
       #Response({'profiles': queryset})