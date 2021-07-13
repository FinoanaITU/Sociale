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
    choice_sexe = models.TextChoices('Masculin','Feminin')

    nom_salarie = models.CharField(max_length=50,null=False)
    prenom_salarie = models.CharField(max_length=50,null=False)
    sexe = models.CharField(blank=True, choices=choice_sexe.choices, max_length=10)
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

    def getIdentification (self):
        return {
            'nomDeNaissance': self.nom_salarie,
            'prenom': self.prenom_salarie,
            'nomMarital': self.nom_maritale,
            'sexe': self.sexe,
            'matricule': self.matricule,
            'matriculeInterne': self.matricule_interne,
            'nir': self.nir,
            'situationFamiliale': self.situation_familiale,
            'dateNaissance': self.date_naissance,
            'paysNaissance': self.pay_naissance,
            'departementNaissance': self.commune_naissance,
        }

class Emploi(models.Model):
    choice_type_salaire = models.TextChoices('Mensuel','Horaire')

    nature_emploi = models.CharField(max_length=50,null=False)
    type_contrat = models.CharField(max_length=20, null=False)
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

    def getEmploi (self):
        return {
        'nature':self.nature_emploi,
        'codeContrat':self.type_contrat,
        'dureeInitialeCDDMois':self.duree_mois,
        'dureeInitialeCDDJours':self.duree_jours,
        'dateDebut':self.date_debut_emploi,
        'motifDebut':self.motif_debut_emploi,
        'dateFin':self.date_fin_emploi,
        'motifFin':self.motif_fin_emploi,
        'code_metier':self.code_metier,
        'salaireBase':self.salaire_brute,
        'salaireType':self.type_salaire,
        'heureMensuellees':self.heure_normale,
    }

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

    def getCoordonnees (self):
        return {
            'voie':self.voie,
            'complement':self.complement,
            'codePostal':self.code_postale,
            'codeVille':self.ville_salarie,
            'address_salarie':self.address_salarie,
            'horsFrance':self.hors_france_salarie,
            'pays':self.pays_code_salarie,
            'paysNom':self.pays_nom_salarie,
            'telDomicile':self.tel_domicile,
            'telBureau':self.tel_bureau,
            'telPortable':self.tel_portable,
            'telPortablePro':self.tel_portable_pros,
            'email':self.email_salarie,
        }
class Salarie (models.Model):
    societe = models.ForeignKey(Societe, on_delete=models.DO_NOTHING,null=True)
    etape_creation = models.OneToOneField(EtapeCreationSalarie,null=True,on_delete=models.CASCADE)
    identification = models.OneToOneField(Identification,null=True,on_delete=models.CASCADE)
    coordonnees = models.OneToOneField(Coordonnees,null=True,on_delete=models.CASCADE)
    emploi = models.OneToOneField(Emploi,null=True,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def getSalarie (self):
        result = ''
        if self.identification != None:
            info = self.identification.getIdentification()
            result = {
                'idSalarie': self.id,
                'nom': info['nomMarital'] if info['nomMarital'] != '' else info['nomDeNaissance'],
                'prenom': info['prenom'],
                'matricule': info['matricule'],
                'dateEntrer': str(self.created_at.date()),
                'statusCreation': self.etape_creation.status() if self.etape_creation != None else False
            }
        else:
            result = {
                'idSalarie': self.id,
                'nom': 'nouvelle salarie_'+str(self.id),
                'prenom': '' ,
                'matricule': '',
                'dateEntrer': str(self.created_at.date()),
                'statusCreation': self.etape_creation.status() if self.etape_creation != None else False
            }
        
        return result
class InformationBancaire(models.Model):
    rib = models.TextField(max_length=20,null=False)
    iban = models.TextField(max_length=20,null=False)
    bic = models.TextField(max_length=20,null=False)
    virement = models.BooleanField(default=False)
    plafond = models.FloatField(null=True)
    salarie = models.ForeignKey(Salarie,on_delete=models.CASCADE)

class Pieces(models.Model):
    nom_piece = models.TextField(max_length=200, null=False)
    salarie = models.ForeignKey(Salarie,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_piece