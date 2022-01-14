from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import MediaType, Member, Genre, Artist, Album, CartProduct, Cart, Order, Customer, Notification, ImageGallery


class MembersInline(admin.TabularInline):

    model = Artist.members.through


class ImageGallaryInline(GenericTabularInline):

    model = ImageGallery
    readonly_fields = ('image_url',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    inlines = [ImageGallaryInline]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    inlines = [MembersInline, ImageGallaryInline]
    exclude = ('members',)

admin.site.register(MediaType)
admin.site.register(Member)
admin.site.register(Genre)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
admin.site.register(ImageGallery)