from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import AgendaForm
from .models import Agenda


def home(request):
    lista = Agenda.objects.order_by('id')
    form = AgendaForm()
    context = {'lista': lista, 'form': form}
    return render (request, 'agenda/home.html', context)


@require_POST
def addAgenda(request):
    form = AgendaForm(request.POST)

    if form.is_valid():
        nova_agenda = Agenda(text=request.POST['text'])
        nova_agenda.save()

    return redirect(home)


def completarTarefa(request, agenda_id):
    agenda = Agenda.objects.get(pk=agenda_id)
    agenda.complete = True
    agenda.save()

    return redirect('home')


def deletarCompleto(request):
    Agenda.objects.filter(complete__exact=True).delete()

    return redirect(home)


def deletarTudo(request):
    Agenda.objects.all().delete()

    return redirect('home')