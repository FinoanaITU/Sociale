from django.db import models
from django.db.models.base import Model

class Societe(models.Model):
    nom_societe = models.TextField(max_length=50,null=False)
    locale = models.TextField(max_length=50,null=False)
    siret = models.CharField(max_length=14,null=False,unique=True)
    activiter = models.TextField(max_length=50,null=False)

    def __str__(self):
        return self.nom_societe

    def getSociete (self):
        return {
            'idSociete': self.id,
            'nomSociete': self.nom_societe,
            'locale': self.locale,
            'activiter': self.activiter,
            'siret': self.siret,
        }