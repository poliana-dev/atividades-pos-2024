from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from api import views

router = routers.DefaultRouter()
router.register(r'artistas', views.ArtistaViewSet)
router.register(r'albuns', views.AlbumViewSet)
router.register(r'musicas', views.MusicaViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)