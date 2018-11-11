"""oauth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from portal.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('users/', UserList.as_view()),
    url('users/<pk>/', UserDetails.as_view()),
    url('groups/', GroupList.as_view()),
]
