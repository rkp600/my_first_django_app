from django.conf.urls import patterns, include, url
from blog.views import *
from django.contrib import admin
 
urlpatterns = patterns('',
    url(r'^admin/',admin.site.urls),
    url(r'',include('blog.urls')),
    (r'^logout/$',{'next_page': '/successfully_logged_out/'}),
    url(r'^accounts/blog/$', 'views.blog'), # If user is not login it will redirect to login page
    url(r'^register/$','simplesite.views.register'),
    url(r'^register/success/$','simplesite.views.register.success'),
    url(r'^home/$', 'simplesite.views.home'),
)
