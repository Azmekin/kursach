from django.contrib import admin
from django.urls import path, include
from .views import ChawoView, TestTemplate
from django.views.generic import TemplateView
urlpatterns = [
path('get_all/', ChawoView.as_view()),
path('help/', TestTemplate.as_view())
]
