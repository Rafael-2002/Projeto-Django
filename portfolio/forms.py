from django.forms import ModelForm
from .models import Cadeira, Projetos, Blog, Comentarios


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'


class ArtigoForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'
