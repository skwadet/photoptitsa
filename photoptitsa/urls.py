from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from photoptitsa_app.views import *
from photoptitsa_app.admin import admin_site


router = DefaultRouter()

router.register(r'examples', ExampleViewSet, basename='exampleapi')
router.register(r'carousel', CarouselViewSet, basename='carouselapi')
router.register(r'tags', TagViewSet, basename='tagapi')
router.register(r'album_previews', AlbumPreviewViewSet, basename='albumpreviewsapi')

urlpatterns = [
    path('admin/', admin_site.urls),
    path('api/', include(router.urls)),
]
