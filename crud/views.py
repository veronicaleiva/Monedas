from django.shortcuts import render, get_object_or_404 ,redirect , reverse  # shortcuts importa las funciones que se usan aqui
from crud.forms import MonedasForm
from .models import Monedas

# Create your views here.
def index(request):

    monedas = Monedas.objects.all().order_by('id') # .order_by('-id') es descendente. para mas campos separar con coma
    context = {'monedas': monedas,
                'titulo': 'Monedas'}
    return render(request, 'crud/index.html',context)

def nuevo(request):
    if request.method == 'POST':
        print ("en POST")
        form = MonedasForm(request.POST)
        if form.is_valid():
            print ("formulario valdo")

            m = {'nombre': form.cleaned_data['nombre'],
                'abreviacion': form.cleaned_data['abreviacion']
                }
            moneda = Monedas()
            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']

            moneda.save()
            print ("Moneda grabada")

            return redirect(reverse('crudindex'))
    else:
        print ("creando nueva moneda")
        form = MonedasForm()

    context = {'formulario':form}
    return render(request, 'crud/nuevo.html',context)

def editar(request, pk):
    moneda = get_object_or_404(Monedas, pk=pk)

    print(moneda)

    # puede ser este código o el parrafo de más abajo
    # en el taller primero lo hicimos asi
    #if request.method == 'GET':
    #    print ("estoy consultabdo")
    #    m = {'nombre': moneda.nombre,
    #        'abreviacion': moneda.abreviacion
    #    }
    #    form = MonedasForm(m)

    #else:
    #    print ("estoy grabando")

    # o este codigo
    if request.method == 'POST':
        print ("estoy grabando")
        form = MonedasForm(request.POST)
        if form.is_valid():
            print ("formulario valdo")

            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']
            moneda.save()

            print ("moneda grabada !!!")
            # return redirect('/crud/')
            return redirect(reverse('crudindex'))
    else:
        print ("estoy consultando")

        m = {'nombre': moneda.nombre,
        'abreviacion': moneda.abreviacion
        }
        form = MonedasForm(m)

    context = {'moneda':moneda, 'formulario': form}
    return render(request, 'crud/editar.html',context)

def eliminar(request, pk):
    moneda = get_object_or_404(Monedas, pk=pk)
    print(moneda)

    if request.method == 'POST':
        print ("en POST de eliminar")

        moneda.delete()
        # moneda.save(). por defecto hace commit autimaticamente, en caso contrario se coloca este comando

        return redirect(reverse('crudindex'))

    else:
        print ("solo miraba, gracias ;)")
        m = {'nombre': moneda.nombre,
        'abreviacion': moneda.abreviacion
        }
        form = MonedasForm(m)

    context = {'moneda':moneda, 'formulario': form}
    return render(request, 'crud/editar.html',context)
