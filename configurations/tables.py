# configurations/tables.py
import django_tables2 as tables
from django_tables2.utils import A
from .models import Conducteur

class ConducteurTable(tables.Table):
    nom = tables.Column(verbose_name="Nom")
    prenom = tables.Column(verbose_name="Prénom")
    date_naissance = tables.DateColumn(
        verbose_name="Date de naissance",
        format="d/m/Y"
    )
    date_embauche = tables.DateColumn(
        verbose_name="Date d'embauche",
        format="d/m/Y"
    )
    
    # Colonnes d'actions (optionnel)
    actions = tables.TemplateColumn(
        template_name='configurations/layout/conducteur_actions.html',
        verbose_name="Actions",
        orderable=False
    )

    class Meta:
        model = Conducteur
        template_name = "django_tables2/bootstrap4.html"
        fields = ("nom", "prenom", "date_naissance", "date_embauche", "actions")
        attrs = {
            "class": "table table-striped table-hover",
            "id": "conducteur-table"
        }
        empty_text = "Aucun conducteur trouvé."

class ConducteurSansDateNaissanceTable(tables.Table):
    # Colonnes personnalisées
    nom = tables.Column(verbose_name="Nom")
    prenom = tables.Column(verbose_name="Prénom")

    date_naissance = tables.DateColumn(
        verbose_name="Date de naissance",
        format="d/m/Y",
        default="Non renseignée"
    )
        
    date_embauche = tables.DateColumn(
        format="d/m/Y", 
        verbose_name="Date d'embauche",
        default="Non renseignée"
    )
    
    # Colonne d'actions (optionnelle)
    actions = tables.TemplateColumn(
        template_name='configurations/layout/conducteur_actions.html',
        verbose_name="Actions",
        orderable=False
    )
    
    class Meta:
        model = Conducteur
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "nom", "prenom", "date_naissance", "date_embauche", "actions")
        attrs = {
            "class": "table table-striped table-hover",
            "th": {"class": "table-dark"}
        }
        empty_text = "Aucun conducteur sans date de naissance trouvé."        
