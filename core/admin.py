from django.contrib import admin
from .models import Objeto
# Register your models here.

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nome','descricao', 'cell', 'email']


