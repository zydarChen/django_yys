from django.conf.urls import url

from . import views

app_name = 'table'
urlpatterns = [
    url(r'^update', views.update),
]