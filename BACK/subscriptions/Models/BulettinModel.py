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
    motifs = models.ManyToManyField(Motifs, through='ModelMotif')

    def __str__(self):
        return self.nom_model

    def getModel (self):
        return{
            'id': self.id,
            'societe': self.societe,
            'nom_model': self.nom_model,
            'motifs': self.motifs,
        }

class ModelMotif(models.Model):
    model = models.ForeignKey(BulletinModel, on_delete= models.CASCADE)
    motif = models.ForeignKey(Motifs, on_delete= models.CASCADE)
    isHaut = models.BooleanField(default=False)
    isBas = models.BooleanField(default=False)