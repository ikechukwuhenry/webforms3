from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import mywikipedia.views

urlpatterns = [
    # Examples:
    url(r'^wikipedia$', 'mywikipedia.views.wikipedia', name='wikipedia'),
    url(r'^customlogin$', 'mywikipedia.views.customLogin', name='clogin'),
    url(r'^profile$', 'mywikipedia.views.profile', name='profile'),
    url(r'^signin$', 'mywikipedia.views.signin', name='signin'),
    url(r'^login$',auth_views.login, {'template_name':'mywikipedia/login.html'}, name='login'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
