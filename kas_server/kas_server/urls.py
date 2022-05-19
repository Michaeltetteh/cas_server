from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cas/', include('cas_server.urls', namespace="cas_server")),
]
