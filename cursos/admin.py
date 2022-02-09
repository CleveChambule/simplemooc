from django.contrib import admin

# Register your models here.
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    #especificamos como vai estar descrito no admin
    list_display = ['nome','slug','start_data','created_at']
    #lista de campos para pesquisar
    search_fields = ['nome','slug']

    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Curso,CursoAdmin)