from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuarios
from cadastro.models import Empresa
from usuarios.forms import UsuarioForm

@login_required
def listar_user(request, empresa_id):
    users = Usuarios.objects.filter(empresa_id=empresa_id).order_by('user')
    empresa = Empresa.objects.get(id=empresa_id)
    return render(request, 'usuarios.html', {'users': users,
                                             'empresa':empresa})

@login_required
def criar_user(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = UsuarioForm(request.POST or None, request.FILES or None, initial={'empresa':id})

    if form.is_valid():
        form.save()
        return redirect('listar_user', empresa_id=id)

    return render(request, 'usuario_form.html', {'form': form, 'empresa': empresa})

@login_required
def atualizar_user(request, id):
    user = get_object_or_404(Usuarios, pk=id)
    empresa = get_object_or_404(Usuarios, pk=user.empresa_id)
    form = UsuarioForm(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('listar_user', empresa_id=empresa.id)
    return render(request, 'usuario_form.html',{'form': form, 'empresa': empresa})

@login_required
def deletar_user(request, empresa_id, id):
    user = get_object_or_404(Usuarios, pk=id)

    if request.method == 'POST':
        user.delete()
        return redirect('listar_user', empresa_id=empresa_id)

    return render(request, 'confirm_delete_empresa.html', {'user': user})

