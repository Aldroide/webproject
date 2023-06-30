from django.contrib import admin
from .models import Producto, CategoriaProd

# Register your models here.


class CatProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


class ProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(CategoriaProd, CatProdAdmin)
admin.site.register(Producto, ProdAdmin)
