
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("", include("main.urls")),
    path('admin/', admin.site.urls)
]
#подключение статических файлов (css)
urlpatterns += staticfiles_urlpatterns()