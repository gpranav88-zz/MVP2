from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check-email', views.check_duplicate_email, name='check_duplicate_email')
]
