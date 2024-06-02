from django.shortcuts import render, redirect, HttpResponse
from .forms import ProyectoForm, ProyectoEForm, CedenteForm, CedenteUForm, ReceptorForm, ReceptorUForm, AccionesForm, AccionesEForm, AsignacionForm, AsignacionUForm
from .models import Proyecto, Acciones, Cedente, Receptor, Asignacion
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import get_template
from xhtml2pdf import pisa

# VISTAS DE PRESUPESTO
def iniciopre(request):
    return render(request, "inicio.html")

# VISTAS DE PRESUPUESTO - PROYECTO
def proyecto(request):
    if request.method == 'POST':
        form9 = ProyectoForm(request.POST)
        if form9.is_valid():
            form9.save()
        else:
            context = {'form9': form9}
            return render(request, 'proyecto.html', context)
    proyectoo = Proyecto.objects.all()
    paginator = Paginator(proyectoo, 14) # 14 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)
    context = {'form9': ProyectoForm(), 'formesp': ProyectoEForm(), 'proyectoo': pagina_actual}
    return render(request, 'proyecto.html', context)

# VISTAS DE PRESUPUESTO - CONSULTAR - PROYECTO
def proyecto_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            proyectoo = Proyecto.objects.filter(nombrep=nombrep)
            paginator = Paginator(proyectoo, 5) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form9': ProyectoForm(), 'formesp': ProyectoEForm(), 'proyectoo': pagina_actual}
        return render(request, 'proyecto.html', context)

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO - PROYECTO
def update_proyecto(request, id):
    queryset = Proyecto.objects.get(id=id)
    form9 = ProyectoEForm(instance=queryset)
    if request.method == 'POST':
        form9 = ProyectoEForm(request.POST, instance=queryset)
        if form9.is_valid():
            form9.save()
            return redirect('/presupuesto/proyecto#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - PROYECTO
def del_proyecto(request, id):
    if request.method == 'POST':
        form9 = Proyecto.objects.get(id=id)
        form9.delete()
        return redirect('/presupuesto/proyecto#deletesuccess')
    
#GENERACION DE PDF PRESUPUESTO - PROYECTO
def generar_pdf(request):
    Proyectoo = Proyecto.objects.all()
    template_path = 'proyectopdf.html'
    context = {'Proyectoo': Proyectoo}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Proyecto.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error' + html)
    return response

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO - PROYECTO
def update_proyecto(request, id):
    queryset = Proyecto.objects.get(id=id)
    form9 = ProyectoEForm(instance=queryset)
    if request.method == 'POST':
        form9 = ProyectoEForm(request.POST, instance=queryset)
        if form9.is_valid():
            form9.save()
            return redirect('/presupuesto/proyecto#updatesuccess')

# VISTAS DE PRESUPUESTO - ACCIONES
def acciones(request):
    if request.method == 'POST':
        form14 = AccionesForm(request.POST)
        if form14.is_valid():
            form14.save()
        else:
            context = {'form14': form14}
            return render(request, 'accionescen.html', context)
    accioness = Acciones.objects.all()
    paginator = Paginator(accioness, 15) # 14 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)
    context = {'form14': AccionesForm(), 'formacc': AccionesEForm(), 'accioness': pagina_actual}
    return render(request, 'accionescen.html', context)

# VISTAS DE PRESUPUESTO - CONSULTAR - ACCIONES
def acciones_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            accioness = Acciones.objects.filter(nombrep=nombrep)
            paginator = Paginator(accioness, 5) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form14': AccionesForm(), 'formesp': AccionesEForm(), 'accioness': pagina_actual}
        return render(request, 'accionescen.html', context)

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO - ACCIONES
def update_acciones(request, id):
    queryset = Acciones.objects.get(id=id)
    form9 = AccionesEForm(instance=queryset)
    if request.method == 'POST':
        form14 = AccionesForm(request.POST, instance=queryset)
        if form14.is_valid():
            form14.save()
            return redirect('/presupuesto/acciones#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - ACCIONES
def del_acciones(request, id):
    if request.method == 'POST':
        form14 = Acciones.objects.get(id=id)
        form14.delete()
        return redirect('/presupuesto/acciones#deletesuccess')

# VISTAS DE GENERAR PDF - PRESUPUESTO - ACCIONES
def acciones_pdf(request):
    accioness = Acciones.objects.all()
    template_path = 'accionespdf.html'
    context = {'accioness': accioness}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Acciones.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error' + html)
    return response

# VISTAS DE PRESUPUESTO - CONSULTAR
def asignacion_consultar(request, accion):
    if accion == 'consultar':
        if 'nombredir' in request.GET:
            nombredir = request.GET['nombredir']
            asignacionn = Asignacion.objects.filter(nombredir=nombredir)
            paginator = Paginator(asignacionn, 15) # 15 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form11': AsignacionForm(), 'formedit': AsignacionUForm(), 'asignacionn': pagina_actual}
        return render(request, 'asignacion.html', context)

# VISTAS DE ACTUALIZACIÓN DE ASIGNACION
def update_asignacion(request, id):
    queryset = Asignacion.objects.get(id=id)
    form11 = AsignacionUForm(instance=queryset)
    if request.method == 'POST':
        form11 = AsignacionUForm(request.POST, instance=queryset)
        if form11.is_valid():
            form11.save()
            return redirect('/presupuesto/asignacion#updatesuccess')

# VISTAS DE ASIGNACIÓN
def asignacion(request):
    if request.method == 'POST':
        form11 = AsignacionForm(request.POST)
        if form11.is_valid():
            form11.save()
        else:
            context = {'form11': form11}
            return render(request, 'asignacion.html', context)
    asignacionn = Asignacion.objects.all()
    paginator = Paginator(asignacionn, 14) # 14 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form11': AsignacionForm(), 'formedit': AsignacionUForm(), 'asignacionn': pagina_actual}
    return render(request, 'asignacion.html', context)

# VISTAS DE PRESUPUESTO - CONSULTAR
def asignacion_consultar(request, accion):
    if accion == 'consultar':
        if 'nombredir' in request.GET:
            nombredir = request.GET['nombredir']
            asignacionn = Asignacion.objects.filter(nombredir=nombredir)
            paginator = Paginator(asignacionn, 15) # 15 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form11': AsignacionForm(), 'formedit': AsignacionUForm(), 'asignacionn': pagina_actual}
        return render(request, 'asignacion.html', context)

# VISTAS DE ELIMINACIÓN DE ASIGNACION
def del_asignacion(request, id):
    if request.method == 'POST':
        form11 = Asignacion.objects.get(id=id)
        form11.delete()
        return redirect('/presupuesto/asignacion#deletesuccess')

# VISTAS DE GENERAR PDF - PRESUPUESTO - ASIGNACION
def asignacion_pdf(request):
    asignacionn = Asignacion.objects.all()
    template_path = 'asignacionpdf.html'
    context = {'asignacionn': asignacionn}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Acciones.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error' + html)
    return response

# VISTAS DE PRESUPUESTO - CEDENTE
def cedente(request):
    if request.method == 'POST':
        form15 = CedenteForm(request.POST)
        if form15.is_valid():
            form15.save()
        else:
            context = {'form15': form15}
            return render(request, 'cedente.html', context)
    cedentee = Cedente.objects.all()
    paginator = Paginator(cedentee, 15) # 14 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form15': CedenteForm(), 'formce': CedenteUForm(), 'cedentee': pagina_actual}
    return render(request, 'cedente.html', context)

# VISTAS DE PRESUPUESTO CEDENTE - CONSULTAR
def cedente_consultar(request, accion):
    if accion == 'consultar':
        if 'partidac' in request.GET:
            partidac = request.GET['partidac']
            cedentee = Cedente.objects.filter(partidac=partidac)
            paginator = Paginator(cedentee, 15) # 15 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form15': CedenteForm(), 'formce': CedenteUForm(), 'cedentee': pagina_actual}
        return render(request, 'cedente.html', context)

# VISTAS DE ACTUALIZACION PRESUPUESTO - CEDENTE  
def update_cedente(request, id):
    queryset = Cedente.objects.get(id=id)
    form15 = CedenteUForm(instance=queryset)
    if request.method == 'POST':
        form15 = CedenteUForm(request.POST, instance=queryset)
        if form15.is_valid():
            form15.save()
            return redirect('/presupuesto/cedente#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - CEDENTE
def del_cedente(request, id):
    if request.method == 'POST':
        form15 = Cedente.objects.get(id=id)
        form15.delete()
        return redirect('/presupuesto/cedente#deletesuccess')
    
# VISTAS DE GENERAR PDF DE PRESUPUESTO - CEDENTE
def cedente_pdf(request):
    cedentee = Cedente.objects.all()
    template_path = 'cedentepdf.html'
    context = {'cedentee': cedentee}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Acciones.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error' + html)
    return response

# VISTAS DE PRESUPUESTO - RECEPTOR
def receptor(request):
    if request.method == 'POST':
        form16 = ReceptorForm(request.POST)
        if form16.is_valid():
            form16.save()
        else:
            context = {'form16':form16}
            return render(request, 'receptor.html', context)
    receptorr = Receptor.objects.all()
    paginator = Paginator(receptorr, 15) # 14 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form16': ReceptorForm(), 'formre': ReceptorUForm(), 'receptorr': pagina_actual}
    return render(request, 'receptor.html', context)

# VISTAS DE PRESUPUESTO RECEPTOR - CONSULTAR
def receptor_consultar(request, accion):
    if accion == 'consultar':
        if 'partidar' in request.GET:
            partidar = request.GET['partidar']
            receptorr = Receptor.objects.filter(partidar=partidar)
            paginator = Paginator(receptorr, 15) # 15 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form16': ReceptorForm(), 'formre': ReceptorUForm(), 'receptorr': pagina_actual}
        return render(request, 'receptor.html', context)

# VISTAS DE ACTUALIZACION PRESUPUESTO - RECEPTOR  
def update_receptor(request, id):
    queryset = Receptor.objects.get(id=id)
    form16 = ReceptorUForm(instance=queryset)
    if request.method == 'POST':
        form16 = ReceptorUForm(request.POST, instance=queryset)
        if form16.is_valid():
            form16.save()
            return redirect('/presupuesto/receptor#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - RECEPTOR
def del_receptor(request, id):
    if request.method == 'POST':
        form16 = Receptor.objects.get(id=id)
        form16.delete()
        return redirect('/presupuesto/receptor#deletesuccess')

# VISTAS DE GENERAR PDF DE PRESUPUESTO - RECEPTOR
def receptor_pdf(request):
    receptorr = Receptor.objects.all()
    template_path = 'receptorpdf.html'
    context = {'receptorr': receptorr}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Acciones.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error' + html)
    return response

