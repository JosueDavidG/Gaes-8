from django.contrib import admin
from .models import ImplementosDeportivos,tamaños,Ropa,productos,productosImplementos

class ropaAdmin(admin.ModelAdmin):
    fields = ('nombre','descripcion','precio')
    list_display = ('__str__', 'slug','created_at')

class implementosAdmin(admin.ModelAdmin):
    fields = ('nombre','descripcion','precio')
    list_display = ('__str__', 'slug','created_at')

@admin.register(ImplementosDeportivos)
class ImplementoDeportivosAdmin(admin.ModelAdmin):
    list_display = ('nombre','marca','descripcion')

@admin.register(tamaños)
class tamañosAdmin(admin.ModelAdmin):
    list_display = ('tamaño',)

@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','talla','precio')

@admin.register(productos)
class productosAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto',)

@admin.register(productosImplementos)
class productosImplementosAdmin(admin.ModelAdmin):
    list_display = ('ImplementoDeportivo',)

