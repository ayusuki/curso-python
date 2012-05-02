from django.contrib import admin

from .models import Publicacao, Credito

class PublicacaoAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    fields = (('tipo', 'id_padrao'), 'titulo', 'num_paginas')
    list_display = ('tipo', 'id_padrao', 'num_paginas', 'titulo')
    
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Credito)
