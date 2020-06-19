from django.db import models
from autoslug import AutoSlugField


class ExampleMain(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.FileField(upload_to='examplesmainpreviews/')

    def __str__(self):
        return 'Example main image N: {id}, name: {name}'.format(id=self.id, name=self.name)


class Carousel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.FileField(upload_to='carouselimages/')

    def __str__(self):
        return 'Carousel image N: {id}, name: {name}'.format(id=self.id, name=self.name)


class Tag(models.Model):
    name = models.CharField(max_length=500, unique=True, default='Альбом')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return 'Tag N: {id}, name: {name}'.format(id=self.id, name=self.name)


class AlbumPreview(models.Model):
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to='albumpreviews/')
    url = models.URLField(max_length=250)
    tag = models.ManyToManyField(Tag, related_name='album')

    def __str__(self):
        return 'Album image N: {id}, name: {name}'.format(id=self.id, name=self.name)
