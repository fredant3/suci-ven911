from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import EmergencyForm
from .models import (
    Emergency,
    Estado,
    Municipio,
    Parroquia,
    Incidencia,
    OrganismoCompetente,
)
from django.views.generic import ListView
from django.utils import timezone


@login_required
def emergency(request):
    emergencies = Emergency.objects.filter(
        user=request.user, datecompleted__isnull=True
    )
    paginator = Paginator(emergencies, 10)  # Show 20 emergencies per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "emergencia/emergency.html",
        {"emergencies": paginator.page(page_number), "page_obj": page_obj},
    )


@login_required
def create_emergency(request):
    if request.method == "GET":
        return render(
            request, "emergencia/create_emergency.html", {"form": EmergencyForm}
        )

    try:
        form = EmergencyForm(request.POST)
        new_emergency = form.save(commit=False)
        new_emergency.user = request.user
        new_emergency.save()
        return redirect("emergency")
    except ValueError:
        return render(
            request,
            "emergencia/create_emergency.html",
            {"form": EmergencyForm, "error": "Please provide valid data"},
        )


@login_required
def completed_emergency(request):
    emergencies = Emergency.objects.filter(
        user=request.user, datecompleted__isnull=False
    )
    paginator = Paginator(emergencies, 10)  # Show 20 emergencies per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "emergencia/emergency.html",
        {"emergencies": paginator.page(page_number), "page_obj": page_obj},
    )


@login_required
def statistics_estado(request):
    labels = []
    data = []

    queryset1 = Estado.objects.order_by("-nombre")
    queryset2 = (
        Emergency.objects.values("id_estado")
        .annotate(my_count=Count("id"))
        .order_by("-id_estado")
    )
    for estado in queryset1:
        labels.append(estado.nombre)

    for emergency in queryset2:
        print(emergency["my_count"])
        data.append(emergency["my_count"])

    return render(
        request, "emergencia/statistics_estado.html", {"labels": labels, "data": data}
    )


@login_required
def statistics_municipio(request):
    labels = []
    data = []

    queryset1 = Municipio.objects.order_by("-nombre")
    queryset2 = (
        Emergency.objects.values("id_municipio")
        .annotate(my_count=Count("id"))
        .order_by("-id_municipio")
    )

    for municipio in queryset1:
        labels.append(municipio.nombre)

    for emergency in queryset2:
        data.append(emergency["my_count"])

    return render(
        request,
        "emergencia/statistics_municipio.html",
        {"labels": labels, "data": data},
    )


@login_required
def statistics_parroquia(request):
    labels = []
    data = []

    queryset1 = Parroquia.objects.order_by("-nombre")
    queryset2 = (
        Emergency.objects.values("id_parroquia")
        .annotate(my_count=Count("id"))
        .order_by("-id_parroquia")
    )

    for parroquia in queryset1:
        labels.append(parroquia.nombre)

    for emergency in queryset2:
        data.append(emergency["my_count"])

    return render(
        request,
        "emergencia/statistics_parroquia.html",
        {"labels": labels, "data": data},
    )


@login_required
def statistics_incidencia(request):
    labels = []
    data = []

    queryset1 = Incidencia.objects.order_by("-tipo")
    queryset2 = (
        Emergency.objects.values("id_incidencia")
        .annotate(my_count=Count("id"))
        .order_by()
    )
    for incidencia in queryset1:
        labels.append(incidencia.tipo)

    for emergency in queryset2:
        data.append(emergency["my_count"])

    return render(
        request,
        "emergencia/statistics_incidencia.html",
        {"labels": labels, "data": data},
    )


@login_required
def statistics_organismo(request):
    labels = []
    data = []

    queryset1 = OrganismoCompetente.objects.order_by("-nombre")
    queryset2 = (
        Emergency.objects.values("id_organismo")
        .annotate(my_count=Count("id"))
        .order_by("-id_organismo")
    )
    for organismo in queryset1:
        labels.append(organismo.nombre)

    for emergency in queryset2:
        data.append(emergency["my_count"])

    return render(
        request,
        "emergencia/statistics_organismo.html",
        {"labels": labels, "data": data},
    )


@login_required
def update_emergency(request, emergency_id):
    if request.method == "GET":
        emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
        form = EmergencyForm(instance=emergency)
        return render(
            request,
            "emergencia/update_emergency.html",
            {"emergency": emergency, "form": form},
        )
    else:
        try:
            emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
            form = EmergencyForm(request.POST, instance=emergency)
            form.save()
            return redirect("emergency")
        except ValueError:
            return render(
                request,
                "emergencia/update_emergency.html",
                {
                    "emergency": emergency,
                    "form": form,
                    "error": "Error updating emergency",
                },
            )


@login_required
def complete_emergency(request, emergency_id):
    emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
    if request.method == "POST":
        emergency.datecompleted = timezone.now()
        emergency.save()
        return redirect("emergency")


@login_required
def delete_emergency(request, emergency_id):
    emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
    if request.method == "POST":
        emergency.delete()
        return redirect("emergency")


class SearchEmergency(ListView):
    model = Emergency
    template_name = "emergencia/emergency.html"
    context_object_name = "emergencies"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Emergency.objects.filter(
            denunciante__icontains=query, user=self.request.user
        )
