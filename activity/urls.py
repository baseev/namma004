from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kisaa.views.home', name='home'),
    # url(r'^kisaa/', include('kisaa.foo.urls')),
    url(r'my-posts/$', 'activity.views.MyPosts'),
    url(r'view-my-post/$', 'activity.views.ViewMyPost'),
    url(r'edit-my-post/$', 'activity.views.EditMyPost'),
    url(r'add-like/$', 'activity.views.SaveLike'),
    url(r'mark-spam-post/$', 'activity.views.SaveSpamPost'),
    url(r'mark-spam-comment/$', 'activity.views.SaveSpamComment'),
    url(r'test/$', 'activity.views.Test'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

