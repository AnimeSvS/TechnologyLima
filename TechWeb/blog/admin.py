from unicodedata import category
from django.contrib import admin
from .models import Categoria, Publicacion

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
class PublicacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
   