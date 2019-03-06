from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import EmpresaForm
from .models import Empresa
from telefones.models import Telefones, Tipo_telefone


# @login_required
# def listar_empresas(request):
#     empresas = Empresa.objects.all().filter(status=1).order_by('razao')
#     tipo_telefone = Tipo_telefone.objects.all()
#     qtd = Empresa.objects.count()
#
#     return render(
#         request, 'empresas.html', {
#             'empresas': empresas,
#             'tipo_telefone': tipo_telefone,
#             'qtd': qtd
#         }
#     )

@login_required
def listar_empresas(request):
    empresas = Empresa.objects.all().filter(status=1).order_by('razao')
    telefones = Telefones.objects.all()
    tipo_telefone = Tipo_telefone.objects.all()
    qtd = Empresa.objects.count()

    return render(
        request, 'empresas.html', {
            'empresas': empresas,
            'tipo_telefone': tipo_telefone,
            'qtd': qtd,
            'telefones':telefones
        }
    )


@login_required
def criar_empresas(request):
    form = EmpresaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_empresas')
    return render(request, 'empresa_form.html', {'form': form})

@login_required
def atualizar(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(request.POST or None, request.FILES or None, instance=empresa)

    if form.is_valid():
        form.save()
        return redirect('listar_empresas')
    return render(request, 'empresa_form.html',{'form': form})

@user_passes_test(lambda u: u.is_superuser)
def deletar(request, id):
    empresa = get_object_or_404(Empresa, pk=id)

    if request.method == 'POST':
        empresa.delete()
        return redirect('listar_empresas')

    return render(request, 'confirm_delete_empresa.html', {'empresa': empresa})

@login_required
def ler(request, id):
    empresa = Empresa.objects.get(pk=id)

    return render(request, 'empresa_dados.html', {'empresa': empresa})
