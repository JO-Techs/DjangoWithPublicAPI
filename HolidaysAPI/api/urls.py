from django.urls import path
from .views import ColorMindAPI, CalendarificAPI, UselessFactAPI

urlpatterns = [
    path('colors/', ColorMindAPI.as_view(), name='colors'),
    path('holidays/', CalendarificAPI.as_view(), name='holidays'),
    path('useless-fact/', UselessFactAPI.as_view(), name='useless-fact'),
]