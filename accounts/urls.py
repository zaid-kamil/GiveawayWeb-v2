from django.conf.urls import url

from accounts.views import show_dash

urlpatterns = [
   url(r'^dashboard/', show_dash, name='dashboard'),

]
