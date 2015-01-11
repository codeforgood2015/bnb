from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings 
from volunteers import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bnbvolunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer/home/$', views.volunteerHome, name="volunteerHome"),
    url(r'^volunteer/home/submit/$', views.volunteerSubmit, name="submitNewLog"),
    url(r'^volunteer/login.html', views.showLoginPage, name="showLoginPage"),
    url(r'^volunteer/authenticatingLogin.html', views.userLogin, name="userLogin"),
)
