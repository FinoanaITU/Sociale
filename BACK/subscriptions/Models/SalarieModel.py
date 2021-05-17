from django.db import models
from django.db.models.base import Model


class EtapeCreationSalarie(models.Model):
    identification = models.BooleanField(default=False)
    coordonnees = models.BooleanField(default=False)
    bancaire = models.BooleanField(default=False)
    emploi = models.BooleanField(default=False)

class Identification(models.Model):
    nom_salarie = models.CharField(max_length=50,null=False)
    prenom_salarie = models.CharField(max_length=50,null=False)
    nom_maritale = models.CharField(max_length=50,null=True)
    matricule = models.CharField(max_length=50,null=True)
    matricule_interne = models.CharField(max_length=50,null=True)
    nir = models.CharField(max_length=15,null=False)
    situation_familiale = models.TextChoices('Marié','Célibataire')
    date_naissance = models.DateField(null=False)
    pay_naissance = models.TextField(max_length=50,null=True)
    commune_naissance = models.TextField(max_length=50,null=True)

class Emploi(models.Model):
    nature_emploi = models.CharField(max_length=50,null=False)
    type_contrat = models.TextField('CDI','CDD')
    duree_mois = models.SmallIntegerField(null=True)
    duree_jours = models.SmallIntegerField(null=True)
    date_debut_emploi = models.DateField(null=False)
    motif_debut_emploi = models.TextField(max_length=250,null=True)
    date_fin_emploi = models.DateField(null=True)
    motif_fin_emploi = models.TextField(max_length=250,null=True)
    code_metier = models.TextField(max_length=10,null=True)
    salaire_brute = models.FloatField(null=False)
    type_salaire = models.TextChoices('Mensuel','Horaire')
    heure_normale = models.FloatField(null=False)


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
    tel_domicile = models.TextField(max_length=20,null=True)
    email_salarie = models.EmailField(max_length=100)


class Salarie (models.Model):
    etape_creation = models.OneToOneField(EtapeCreationSalarie,null=True,on_delete=models.CASCADE)
    identification = models.OneToOneField(Identification,null=True,on_delete=models.CASCADE)
    coordonnees = models.OneToOneField(Coordonnees,null=True,on_delete=models.CASCADE)
    empoi = models.OneToOneField(Emploi,null=True,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

class InformationBancaire(models.Model):
    rib = models.TextField(max_length=20,null=False)
    iban = models.TextField(max_length=20,null=False)
    bic = models.TextField(max_length=20,null=False)
    virement = models.BooleanField(default=False)
    plafond = models.FloatField(null=True)
    salarie = models.ForeignKey(Salarie,on_delete=models.CASCADE)