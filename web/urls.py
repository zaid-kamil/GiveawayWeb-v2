from django.conf.urls import url

from web.views import view_contact, about
from web.views import show_home

urlpatterns = [
    url(r'^$', show_home, name='home'),
    url(r'^&', view_contact, name='contact'),
    url(r'^$', about, name='about')
]
