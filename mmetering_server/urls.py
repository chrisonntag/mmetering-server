"""mmetering_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required

import mmetering.views as views

urlpatterns = [
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^admin/login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^$', permission_required("mmetering.can_view")(views.IndexView.as_view()), name="home"),
    url(r'^dashboard/$', permission_required("mmetering.can_view")(views.IndexView.as_view()), name="home"),
    url(r'^download/', permission_required("mmetering.can_download")(views.DownloadView.as_view()), name="download"),
    url(r'^contact/', views.ContactView.as_view(), name="contact"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', admin.site.login),  # used for making permission_required decorator work
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/loadprofile/$', views.APILoadProfileView.as_view()),
    url(r'^api/overview/$', views.APIDataOverviewView.as_view()),
]
