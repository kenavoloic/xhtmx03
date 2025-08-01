from django.db import models

class Conducteur(models.Model):
    nom = models.CharField(max_length=255, verbose_name="nom")
    prenom = models.CharField(max_length=255, verbose_name="prenom")
    date_naissance = models.DateField(null=True, blank=True)
    date_embauche = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
# Create your models here.
