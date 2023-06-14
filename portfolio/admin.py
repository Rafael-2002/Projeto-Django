from django.contrib import admin

from.models import Cadeira
from.models import Projetos
from.models import Blog
from.models import Comentarios
# Register your models here.
admin.site.register(Cadeira)
admin.site.register(Projetos)
admin.site.register(Blog)
admin.site.register(Comentarios)
