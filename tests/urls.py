from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'tickets', views.TicketViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^raw/$', views.RawViewSet.as_view(), name='raw-data'),
]
