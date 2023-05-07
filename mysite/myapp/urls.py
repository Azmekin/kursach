from django.contrib import admin
from django.urls import path, include
from .views import ChawoView, TestTemplate, LkTemplate, MyTokenObtainPairView
from django.views.generic import TemplateView
urlpatterns = [
path('get_all/', ChawoView.as_view()),
path('help/', TestTemplate.as_view()),
path('lk/', LkTemplate.as_view()),
path("tokencock/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
