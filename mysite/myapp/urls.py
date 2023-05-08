from django.contrib import admin
from django.urls import path, include
from .views import ChawoView, TestTemplate, LkTemplate, MyTokenObtainPairView, CreateUserView, CreateVallet,CreateOwner,CreateGood,MainTemplate
from django.views.generic import TemplateView
urlpatterns = [
path('get_all/', ChawoView.as_view()),
path('help/', TestTemplate.as_view()),
path('lk/', LkTemplate.as_view()),
path('lk/owner_c/', CreateOwner.as_view()),
path('lk/vallet_c/', CreateVallet.as_view()),
path('lk/good_c', CreateGood.as_view()),
path('register/', CreateUserView.as_view()),
path('mainmenu/', MainTemplate.as_view()),
path("tokencookie/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
