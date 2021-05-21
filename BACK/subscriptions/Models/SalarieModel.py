from django.db import models
from django.db.models.base import Model
from .SocieteModel import Societe
class EtapeCreationSalarie(models.Model):
    identification = models.BooleanField(default=False)
    coordonnees = models.BooleanField(default=False)
    bancaire = models.BooleanField(default=False)
    emploi = models.BooleanField(default=False)

    def status(self):
        if self.identification and self.coordonnees and self.bancaire and self.emploi:
            return True
        else:
            return False

class Identification(models.Model):
    choice_situation_familiale = models.TextChoices('Marié','Célibataire')

    nom_salarie = models.CharField(max_length=50,null=False)
    prenom_salarie = models.CharField(max_length=50,null=False)
    nom_maritale = models.CharField(max_length=50,null=True)
    matricule = models.CharField(max_length=50,null=True)
    matricule_interne = models.CharField(max_length=50,null=True)
    nir = models.CharField(max_length=15,null=False)
    situation_familiale = models.CharField(blank=True, choices=choice_situation_familiale.choices, max_length=15)
    date_naissance = models.DateField(null=False)
    pay_naissance = models.TextField(max_length=50,null=True)
    commune_naissance = models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.nom_salarie

class Emploi(models.Model):
    choice_type_contrat = models.TextChoices('CDI','CDD')
    choice_type_salaire = models.TextChoices('Mensuel','Horaire')

    nature_emploi = models.CharField(max_length=50,null=False)
    type_contrat = models.CharField(blank=True, choices=choice_type_contrat.choices, max_length=3)
    duree_mois = models.SmallIntegerField(null=True)
    duree_jours = models.SmallIntegerField(null=True)
    date_debut_emploi = models.DateField(null=False)
    motif_debut_emploi = models.TextField(max_length=250,null=True)
    date_fin_emploi = models.DateField(null=True)
    motif_fin_emploi = models.TextField(max_length=250,null=True)
    code_metier = models.TextField(max_length=10,null=True)
    salaire_brute = models.FloatField(null=False)
    type_salaire = models.CharField(blank=True, choices=choice_type_salaire.choices, max_length=10)
    heure_normale = models.FloatField(null=False)

    def __str__(self):
        return self.nature_emploi


class Coordonnees(models.Model):
    voie = models.TextField(max_length=50,null=True)
    complement = models.TextField(max_length=50,null=True)
    code_postale = models.TextField(max_length=50,null=True)
    ville_salarie = models.TextField(max_length=50,null=True)
    address_salarie = models.TextField(max_length=50,null=True)
    hors_france_salarie = models.BooleanField(default=False)
    pays_code_salarie = models.TextField(max_length=4,null=True)
    pays_nom_salarie = models.TextField(max_length=50,null=True)
    tel_domicile = models.TextField(max_length=20,null=True)
    tel_bureau = models.TextField(max_length=20,null=True)
    tel_portable = models.TextField(max_length=20,null=True)
    tel_portable_pros = models.TextField(max_length=20,null=True)
    email_salarie = models.EmailField(max_length=100)


    def __str__(self):
        return self.voie

class Salarie (models.Model):
    societe = models.ForeignKey(Societe, on_delete=models.DO_NOTHING,null=True)
    etape_creation = models.OneToOneField(EtapeCreationSalarie,null=True,on_delete=models.CASCADE)
    identification = models.OneToOneField(Identification,null=True,on_delete=models.CASCADE)
    coordonnees = models.OneToOneField(Coordonnees,null=True,on_delete=models.CASCADE)
    emploi = models.OneToOneField(Emploi,null=True,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

class InformationBancaire(models.Model):
    rib = models.TextField(max_length=20,null=False)
    iban = models.TextField(max_length=20,null=False)
    bic = models.TextField(max_length=20,null=False)
    virement = models.BooleanField(default=False)
    plafond = models.FloatField(null=True)
    salarie = models.ForeignKey(Salarie,on_delete=models.CASCADE)

    def __str__(self):
        return self.salarie