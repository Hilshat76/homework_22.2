from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('article/', include('article.urls', namespace='article')),
    path('users/', include('users.urls', namespace='users')),
]
