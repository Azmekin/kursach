from profile import Profile

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from .models import OwnerAdd, Vallet, Goods
from .serializers import ChawoSerializer, Chawo, UserSerializer, ValletSerializer, OwnerSerializer, GoodSerializer


class CreateVallet(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ValletSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(money=5)


class CreateOwner(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OwnerSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save(mark=5)


class CreateGood(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GoodSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class ChawoView(generics.ListAPIView):
    serializer_class = ChawoSerializer
    queryset = Chawo.objects.all()


class AllView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mainmenu.html'

    def get(self, request):
        a = request.query_params
        if a:
            pass
        else:
            a = {'a': ''}
        queryset = Chawo.objects.all()
        a = Goods.objects.filter(id=a['a'])
        return render(request, 'index.html', {'posts': queryset, 'answ': a})


class TestTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        a = request.query_params
        if a:
            pass
        else:
            a = {'a': 1}
        queryset = Chawo.objects.all()
        a = Chawo.objects.filter(id=a['a'])
        return render(request, 'index.html', {'posts': queryset, 'answ': a})
        # Response({'profiles': queryset})






class MainTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mainmenu.html'
    def get(self, request):
        q=request.query_params
        print(q)
        #if q:
        #    pass
        #else:
        #    q = {'vbtn_radio': 1, 'rate' : 3, 'flexRadioDefault' : 1}
        try:
            vbtn_radio=q['vbtn_radio']
        except Exception as e:
            vbtn_radio = 1
        print(vbtn_radio)
        try:
            if q['flexRadioDefault'] == '1':
                flexRadioDefault = True
            else:
                flexRadioDefault = False
        except Exception as e:
            flexRadioDefault=True


        try:
            rate=q['rate']
        except Exception as e:
            rate = 5
        try:
            search=q['search']
            print(search)
        except Exception as e:
            search=''
        print(search)
        queryset = list(Goods.objects.values_list('Name','cost','image','owner','sold_type','IS_3D','IS_2D','IS_AUDIO'))
        GS=[]
        param=''
        if vbtn_radio=='1':
            param=6
        elif vbtn_radio=='2':
            param=7
        else:
            param=5

        for i in queryset:
            print (i)
            if i[4]==flexRadioDefault and i[param]==True and search in i[0]:
                GS.append(i)

        #GS=queryset
        return render(request, 'mainmenu.html', {'goods': GS} )










class LkTemplate(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = 'lk.html'

    def get(self, request):
        a = request.user
        print(request.COOKIES.get("acces"))
        OA = OwnerAdd.objects.filter(owner=a)
        VT = Vallet.objects.filter(owner=a)
        GS = Goods.objects.filter(owner=a)
        if OA:
            pass
        else:
            OA = [{'mark': 0, 'img_res': '', 'owner': a}]
        if VT:
            pass
        else:
            VT = [{'web': '', 'money': 0, 'vallet_number': '0', 'owner': a}]
        if GS:
            pass
        else:
            GS = []
        print(OA, VT, GS)
        return render(request, 'lk.html', {'user': OA[0], 'wallet': VT[0], 'goods': GS})
        # Response({'profiles': queryset})


from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        response.set_cookie("acces", token, httponly=True)
        return response
