from rest_framework import serializers
from .models import ExampleMain, Carousel, Tag, AlbumPreview


class ExampleMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleMain
        fields = ('name', 'image')


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ('name', 'image')


class AlbumPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPreview
        fields = ('name', 'image', 'url', 'tag')


class TagSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Tag
        fields = ['name', 'slug', 'album']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
