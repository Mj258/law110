from django.conf.urls import patterns, include, url
from django.contrib import admin
# from * import markdown2

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^markdown/', include("django_markdown.urls")),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^', include('law119.urls')),
)
