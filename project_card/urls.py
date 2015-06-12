from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^business/', include('company.urls')),
    url(r'^user/', include('user.urls')),
]
