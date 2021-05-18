from django.db import models
from django.db.models.base import Model

class Societe(models.Model):
    nom_societe = models.TextField(max_length=50,null=False)
    locale = models.TextField(max_length=50,null=False)
    siret = models.TextField(max_length=14,null=False)
    activiter = models.TextField(max_length=50,null=False)

    def __str__(self):
        return self.nom_societe