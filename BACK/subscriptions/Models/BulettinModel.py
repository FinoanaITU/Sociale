from django.db.models.deletion import CASCADE
from subscriptions.Models.SalarieModel import Salarie
from django.db import models
from .SocieteModel import Societe

class Motifs(models.Model):
    libelle_motif = models.CharField(max_length=100,null=False)
    isPrime = models.BooleanField(default=False)
    isAbsence = models.BooleanField(default=False)
    isHeure = models.BooleanField(default=False)
    isIndemniter = models.BooleanField(default=False)
    isAutre = models.BooleanField(default=False)

    def __str__(self):
        return self.libelle_motif
        

class BulletinModel(models.Model):
    societe = models.ForeignKey(Societe, on_delete = models.CASCADE)
    nom_model = models.CharField(max_length=100, null=True)
    motifs = models.ManyToManyField(Motifs)

    def __str__(self):
        return self.nom_model