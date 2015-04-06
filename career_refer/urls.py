from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'career_refer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'User.views.index'),
    #url(r'^career_refer/template/$', 'User.views.template'),
    #url(r'^career_refer/register/$', 'User.views.register'),
    #url(r'^career_refer/login/$', 'User.views.login'),
    #url(r'^career_refer/logout/$', 'User.views.logout'),

)
