from django.contrib import admin
from .models import *
from certificados.models import *
from usuarios.models import *
from telefones.models import *
from mapas.models import *

admin.site.register(Empresa)
admin.site.register(Telefones)
admin.site.register(Usuarios)
admin.site.register(Tipo_status)
admin.site.register(Tipo_certificado)
admin.site.register(Tipo_telefone)
admin.site.register(Tipo_usuario)
admin.site.register(Nota)
