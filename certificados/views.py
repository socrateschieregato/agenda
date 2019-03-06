from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from certificados.models import Certificados
from cadastro.models import Empresa
from certificados.forms import CertificadosForm, CertificadoForm
from datetime import date

@login_required
def listar_cert_todos(request):
    certificados = Certificados.objects.all()
    empresas = Empresa.objects.all()
    hoje = date.today()

    return render(request, 'certificados_todos.html', {'certificados': certificados,
                                                       'empresas':empresas,
                                                       'hoje':hoje})

@login_required
def listar_certificados(request, empresa_id):
    certificados = Certificados.objects.filter(empresa_id=empresa_id)
    empresa = Empresa.objects.get(id=empresa_id)
    hoje = date.today()

    return render(request, 'certificados.html', {'certificados': certificados,
                                                 'empresa':empresa,
                                                 'hoje': hoje,
                                                 })

@login_required
def criar_certificado_cliente(request, id):
    form = CertificadosForm(request.POST or None, request.FILES or None, initial={'empresa':id})
    empresa = Empresa.objects.get(id=id)

    if form.is_valid():
        form.save()
        return redirect('listar_certificados', empresa_id=id)
    return render(request, 'certificado_form.html', {'form': form, 'empresa':empresa})

@login_required
def criar_certificado(request):
    form = CertificadoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cert_todos')
    return render(request, 'certificado_form.html', {'form': form})

@login_required
def atualizar_certificado(request, id):
    cert = get_object_or_404(Certificados, pk=id)
    form = CertificadosForm(request.POST or None, request.FILES or None, instance=cert)

    if form.is_valid():
        form.save()
        return redirect('listar_certificados', empresa_id=cert.empresa_id)
    return render(request, 'certificado_form.html',{'form': form})

@login_required
def deletar_certificado(request, empresa_id, id):
    certificado = get_object_or_404(Certificados, pk=id)

    if request.method == 'POST':
        certificado.delete()
        return redirect('listar_certificados', empresa_id=empresa_id)

    return render(request, 'confirm_delete_certificado.html', {'certificado': certificado})

def validar_certificado(request, id):
    certificado = get_object_or_404(Certificados, pk=id)
