from django.shortcuts import render, redirect
from .forms import FiscalForm
from .models import Nota, Fiscal
import xlrd


def abrir_planilha(path):
    book = xlrd.open_workbook(path)

    # print number of sheets
    print (book.nsheets)

    # print sheet names
    print (book.sheet_names())

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    # read a row
    print (first_sheet.row_values(0))

    # read a cell
    cell = first_sheet.cell(0, 0)
    print (cell)
    print (cell.value)

    # read a row slice
    print (first_sheet.row_slice(rowx=0,
                                 start_colx=0,
                                 end_colx=2)
           )

def listar_notas(request):
    pass

def listar_planilhas(request):
    planilhas = Fiscal.objects.all()
    qtd = Fiscal.objects.count()

    return render(
        request, 'notas.html', {
            'planilhas': planilhas,
            'qtd': qtd
        }
    )


def nova_planilha(request):
    form = FiscalForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        print('válido')
        return redirect('listar_planilhas')
    print('inválido')
    return render(request, 'mapas_form.html', {'form': form})