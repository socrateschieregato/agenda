from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from telefones.models import Telefones
from cadastro.models import Empresa
from telefones.forms import TelefoneForm

@login_required
def listar_telefones(request, empresa_id):
    telefones = Telefones.objects.filter(empresa_id=empresa_id).order_by('pessoa')
    empresa = Empresa.objects.get(id=empresa_id)
    return render(request, 'telefone.html', {'telefones': telefones, 'empresa':empresa})

@login_required
def criar_telefones(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = TelefoneForm(request.POST or None, request.FILES or None, initial={'empresa':id})

    if form.is_valid():
        form.save()
        return redirect('listar_telefones', empresa_id=id)

    return render(request, 'telefone_form.html', {'form': form, 'empresa': empresa})

@login_required
def atualizar_telefones(request, id):
    telefones = get_object_or_404(Telefones, pk=id)
    empresa = get_object_or_404(Empresa, pk=telefones.empresa_id)
    form = TelefoneForm(request.POST or None, request.FILES or None, instance=telefones)

    if form.is_valid():
        form.save()
        return redirect('listar_telefones', empresa_id=empresa.id)
    return render(request, 'telefone_form.html',{'form': form, 'empresa': empresa})

@login_required
def deletar_telefones(request, empresa_id, id):
    telefone = get_object_or_404(Telefones, pk=id)

    if request.method == 'POST':
        telefone.delete()
        return redirect('listar_telefones', empresa_id=empresa_id)

    return render(request, 'confirm_delete_telefone.html', {'telefone': telefone})
