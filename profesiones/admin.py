from django.contrib import admin
from profesiones.models import Licenciado, Ingeniero, Medico
# Register your models here.

admin.site.register(Licenciado)
admin.site.register(Ingeniero)
admin.site.register(Medico)