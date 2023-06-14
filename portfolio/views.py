from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import CadeiraForm, ProjetosForm, ArtigoForm, ComentarioForm
from .models import Cadeira
from .models import Projetos
from .models import User
from .models import Blog
from .models import Comentarios


@login_required
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    cadeira = Cadeira.objects.all()
    projetos = Projetos.objects.all()
    return render(request, 'index.html', {'cadeira': cadeira, 'projetos': projetos})


def blog(request):
    blog = Blog.objects.all()
    comentarios = Comentarios.objects.all()
    return render(request, 'blog.html', {'blog': blog, 'comentarios': comentarios})


def javascript(request):
    return render(request, 'javascript.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'message': "Logged out"})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, "login.html", {'message': "Invalid credentials"})

    return render(request, "login.html")


def cadeiraNova(request):
    form = CadeiraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}
    return render(request, 'cadeiraNova.html', context)


def projetoNovo(request):
    form = ProjetosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}
    return render(request, 'projetoNovo.html', context)


def editarCadeira(request, cadeira_id):
    cadeira = Cadeira.objects.get(pk=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'editarCadeira.html', context)


def editarProjeto(request, projetos_id):
    projetos = Projetos.objects.get(pk=projetos_id)
    form = ProjetosForm(request.POST or None, instance=projetos)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form, 'projetos_id': projetos_id}
    return render(request, 'editarProjeto.html', context)


def apagarCadeira(request, cadeira_id):
    Cadeira.objects.get(pk=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))


def apagarProjeto(request, projetos_id):
    Projetos.objects.get(pk=projetos_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))


def artigoNovo(request):
    form = ArtigoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'adicionarArtigo.html', context)


def comentarioNovo(request):
    form = ComentarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'comentarioNovo.html', context)
