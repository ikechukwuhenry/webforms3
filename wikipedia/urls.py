from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
#import mywikipedia.views

urlpatterns = patterns('mywikipedia.views',
    # Examples:
    url(r'^home$', 'home', name='home'),
    url(r'^wikipedia$', 'wikipedia', name='wikipedia'),
    url(r'^customlogin$', 'customLogin', name='clogin'),
    url(r'^profile$', 'profile', name='profile'),
    url(r'^signin$', 'signin', name='signin'),
    url(r'^contactus$', 'contact_us', name='contactus'),
    url(r'^login$',auth_views.login, {'template_name':'mywikipedia/login.html'}, name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/login/$', 'login', {'template_name':'mywikipedia/login.html'}, name='user/login'),

    url(r'^admin/', include(admin.site.urls)),
)
