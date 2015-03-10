from django.conf.urls import patterns, include, url

from .import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'law119.views.home', name='home'),
    url(r'^$', views.home.as_view(),name="index"),

)
