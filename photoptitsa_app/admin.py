from django.contrib import admin
from .models import ExampleMain, Carousel, Tag, AlbumPreview


class MyAdminSite(admin.AdminSite):
    site_header = 'Фотоптица'
    site_title = 'фотоптица - администрирование'
    index_title = 'Добро пожаловать'


admin_site = MyAdminSite(name='myadmin')
admin_site.register(ExampleMain)
admin_site.register(Carousel)
admin_site.register(Tag)
admin_site.register(AlbumPreview)
