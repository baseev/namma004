from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kisaa.views.home', name='home'),
    # url(r'^kisaa/', include('kisaa.foo.urls')),
    url(r'home/$', 'main.views.Home'),
    url(r'my-profile/$', 'main.views.Profile'),
    url(r'channel-error/$', 'main.views.ChannelError'),
    url(r'new-social-user/$', 'main.views.NewSocialUser'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

