from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import ExampleMainSerializer, CarouselSerializer, AlbumPreviewSerializer, TagSerializer
from rest_framework.views import exception_handler
from .models import ExampleMain, Carousel, Tag, AlbumPreview


class ExampleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ExampleMain.objects.all()
    serializer_class = ExampleMainSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class AlbumPreviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = AlbumPreview.objects.all()
    serializer_class = AlbumPreviewSerializer
