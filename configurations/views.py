from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import Conducteur
from .tables import ConducteurTable
from .forms import ConducteurForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'configurations/pages/login.html'
    redirect_authenticated_user = True

def tableau_de_bord(request):
    return render(request, 'configurations/pages/tableau.html')

#ne marche que si DEBUG = FALSE, sinon gestion générique par Django
def page_inconnue(request, exception):
    if request.user.is_authenticated:
        return redirect("tableau")
    else:
        return redirect("login")

def conducteur_list(request):
    """Vue principale pour afficher la liste des conducteurs"""
    conducteurs = Conducteur.objects.all()
    table = ConducteurTable(conducteurs)
    
    # Configuration de la pagination et du tri
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    
    # Si c'est une requête HTMX, on retourne seulement le tableau
    if request.headers.get('HX-Request'):
        return render(request, 'configurations/pages/conducteur_table_partial.html', {
            'table': table
        })
    
    # Sinon, on retourne la page complète
    return render(request, 'configurations/pages/conducteur_list.html', {
        'table': table
    })

def conducteur_search(request):
    """Vue pour la recherche HTMX"""
    query = request.GET.get('q', '')
    
    if query:
        conducteurs = Conducteur.objects.filter(
            nom__icontains=query
        ) | Conducteur.objects.filter(
            prenom__icontains=query
        )
    else:
        conducteurs = Conducteur.objects.all()
    
    table = ConducteurTable(conducteurs)
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    
    return render(request, 'configurations/pages/conducteur_table_partial.html', {
        'table': table
    })

def conducteur_edit(request, pk):
    """Vue pour modifier un conducteur"""
    conducteur = get_object_or_404(Conducteur, pk=pk)
    
    if request.method == 'POST':
        form = ConducteurForm(request.POST, instance=conducteur)
        if form.is_valid():
            form.save()
            # Retourner le tableau mis à jour
            conducteurs = Conducteur.objects.all()
            table = ConducteurTable(conducteurs)
            RequestConfig(request, paginate={"per_page": 25}).configure(table)
            
            return render(request, 'configurations/pages/conducteur_table_partial.html', {
                'table': table
            })
    else:
        form = ConducteurForm(instance=conducteur)
    
    return render(request, 'configurations/pages/conducteur_edit_modal.html', {
        'form': form,
        'conducteur': conducteur
    })
