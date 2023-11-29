from django.urls import path
from . import views

urlpatterns = [
    path('voiceasst/', views.voiceasst, name='voiceasst'),
]