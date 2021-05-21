from subscriptions.Models.SocieteModel import Societe
from ..Models.SalarieModel import Emploi, Salarie 
from ..Models.SalarieModel import Identification
from ..Models.SalarieModel import EtapeCreationSalarie
from ..Models.SalarieModel import Coordonnees
from ..Models.SalarieModel import InformationBancaire

class GestionSalarie():
    def __init__(self):
        self.societe = Societe.objects.get(id=1)
    
    def checkSalarie(self,idSalarie):
        salarie = None
        try:
            salarie =  Salarie.objects.get(id=idSalarie)
        except Exception as e:
            print(e)
        
        return salarie

    def majEtape(self,Salarie,actionName):
        result = None
        etape = Salarie.etape_creation
        if etape == None:
            try:
                newEtape = EtapeCreationSalarie.objects
                if actionName == 'identification':
                    newEtape = newEtape.create(identification=True)
                elif actionName == 'coordonnees':
                    newEtape = newEtape.create(coordonnees=True)
                elif actionName == 'infoBank':
                    newEtape = newEtape.create(bancaire=True)
                elif actionName == 'infoEmploi':
                    newEtape = newEtape.create(emploi=True)
                result = newEtape
            except Exception as e:
                print(e)
        else:
            try:
                upEtape = etape
                if actionName == 'identification':
                    upEtape.identification=True
                elif actionName == 'coordonnees':
                    upEtape.coordonnees = True
                elif actionName == 'infoBank':
                    upEtape.bancaire = True
                elif actionName == 'infoEmploi':
                    upEtape.emploi = True
                result = upEtape
            except Exception as e:
                print(e)  
        return result

    def ajoutIdentification(self,data):
        result = False
        salarie = self.checkSalarie(8)
        if (salarie == None) or (salarie != None and salarie.identification == None):
            try:
                identifaction = Identification.objects.create(
                    nom_salarie = data['nomDeNaissance'],
                    prenom_salarie = data['prenom'],
                    nom_maritale = data['nomMarital'],
                    matricule = data['matricule'],
                    matricule_interne = data['matriculeInterne'],
                    nir = data['nir'],
                    situation_familiale = data['situationFamiliale'],
                    date_naissance = data['dateNaissance'],
                    pay_naissance = data['paysNaissance'],
                    commune_naissance = data['departementNaissance'],
                )
                print(self.societe,'ato-------------------')
                newSalarier = Salarie()
                newSalarier.identification = identifaction
                newSalarier.societe = self.societe
                etape = self.majEtape(newSalarier,'identification')
                newSalarier.etape_creation = etape
                newSalarier.save()
                result = True
            except Exception as e:
                print(e)
        else:
            result = self.updateIdentification(salarie,data)
        
        return result

    def updateIdentification(self,salarie,data):
        result = False
        upIdentification = salarie.identification
        try:
            upIdentification.nom_salarie = data['nomDeNaissance']
            upIdentification.prenom_salarie = data['prenom']
            upIdentification.nom_maritale = data['nomMarital']
            upIdentification.matricule = data['matricule']
            upIdentification.matricule_interne = data['matriculeInterne']
            upIdentification.nir = data['nir']
            upIdentification.situation_familiale = data['situationFamiliale']
            upIdentification.date_naissance = data['dateNaissance']
            upIdentification.pay_naissance = data['paysNaissance']
            upIdentification.commune_naissance = data['departementNaissance']
            upIdentification.save()
            etape = self.majEtape(salarie,'identification')
            salarie.etape_creation = etape
            salarie.save()
            result = True
        except Exception as e:
            print(e)

        return result


    
    def ajoutCoordonnees(self,data):
        resultat = False
        salarie = self.checkSalarie(9)
        if (salarie == None) or (salarie != None and salarie.coordonnees == None):
            print('ato------------')
            try:
                coordonne = Coordonnees.objects.create(
                    voie = data['voie'],
                    complement = data['complement'],
                    code_postale = data['codePostal'],
                    ville_salarie = data['codeVille'],
                    address_salarie = 'null',
                    hors_france_salarie = data['horsFrance'],
                    pays_code_salarie = data['pays'],
                    pays_nom_salarie = data['paysNom'],
                    tel_domicile = data['telDomicile'],
                    tel_bureau = data['telBureau'],
                    tel_portable = data['telPortable'],
                    tel_portable_pros = data['telPortablePro'],
                    email_salarie = data['email'],
                )
                newSalarier = Salarie()
                newSalarier.coordonnees = coordonne
                newSalarier.societe = self.societe
                etape = self.majEtape(newSalarier,'coordonnees')
                newSalarier.etape_creation = etape
                newSalarier.save()
                resultat = True
            except Exception as e:
                print(e)
        else:
            resultat = self.updateCoordonnees(salarie,data)            
        return resultat
        
    def updateCoordonnees(self,salarie,data):
        result = False
        upCoordonenee = salarie.coordonnees
        try:
            upCoordonenee.voie = data['voie']
            upCoordonenee.complement = data['complement']
            upCoordonenee.code_postale = data['codePostal']
            upCoordonenee.ville_salarie = data['codeVille']
            upCoordonenee.address_salarie = 'null'
            upCoordonenee.hors_france_salarie = data['horsFrance']
            upCoordonenee.pays_code_salarie = data['pays']
            upCoordonenee.pays_nom_salarie = data['paysNom']
            upCoordonenee.tel_domicile = data['telDomicile']
            upCoordonenee.tel_bureau = data['telBureau']
            upCoordonenee.tel_portable = data['telPortable']
            upCoordonenee.tel_portable_pros = data['telPortablePro']
            upCoordonenee.email_salarie = data['email']
            upCoordonenee.save()
            result = True
        except Exception as e:
            print(e)

        return result


    def ajoutEmploi(self,data):
        resultat = False
        salarie = self.checkSalarie(10)
        if (salarie == None) or (salarie != None and salarie.emploi == None):
            print(data)
            try:
                emploi = Emploi.objects.create(
                    nature_emploi = data['nature'],
                    type_contrat = data['codeContrat'],
                    duree_mois = data['dureeInitialeCDDMois'],
                    duree_jours = data['dureeInitialeCDDJours'],
                    date_debut_emploi = data['dateDebut'],
                    motif_debut_emploi = data['motifDebut'],
                    date_fin_emploi = None if data['dateFin'] == '' else data['dateFin'],
                    motif_fin_emploi = data['motifFin'],
                    code_metier = data['codeClassification'],
                    salaire_brute = data['salaireBase'],
                    type_salaire = data['salaireType'],
                    heure_normale = data['heureMensuellees'],
                )
                newSalarier = Salarie()
                newSalarier.emploi = emploi
                newSalarier.societe = self.societe
                etape = self.majEtape(newSalarier,'infoEmploi')
                newSalarier.etape_creation = etape
                newSalarier.save()
                resultat = True
            except Exception as e:
                print(e)
        else:
            resultat = self.updateEmploi(salarie,data)            
        return resultat
        
    def updateEmploi(self,salarie,data):
        result = False
        upEmploi = salarie.emploi
        print('update')
        try:
            upEmploi.nature_emploi = data['nature']
            upEmploi.type_contrat = data['codeContrat']
            upEmploi.duree_mois = data['dureeInitialeCDDMois']
            upEmploi.duree_jours = data['dureeInitialeCDDJours']
            upEmploi.date_debut_emploi = data['dateDebut']
            upEmploi.motif_debut_emploi = data['motifDebut']
            upEmploi.date_fin_emploi = None if data['dateFin'] == '' else data['dateFin'] 
            upEmploi.motif_fin_emploi = data['motifFin']
            upEmploi.code_metier = data['codeClassification']
            upEmploi.salaire_brute = data['salaireBase']
            upEmploi.type_salaire = data['salaireType']
            upEmploi.heure_normale = data['heureMensuellees']
            upEmploi.save()
            result = True
        except Exception as e:
            print(e)

        return result

    def ajoutInfoBank(self,data):
        resultat = False
        salarie = self.checkSalarie(10)
        if salarie != None:
            infoBank = InformationBancaire.objects.filter(salarie= 10)
            if len(infoBank) == 0:
                print(salarie)
                for bankList in data:
                    try:
                        newInfoBank = InformationBancaire.objects.create(
                            bic = bankList['BIC'], 
                            iban = bankList['IBAN'], 
                            rib = bankList['RIB'], 
                            virement = bankList['virement'], 
                            plafond = bankList['plafond'],
                            salarie = salarie
                        )
                        newInfoBank.save()
                        resultat = True
                    except Exception as e:
                        print(e)
            else:
                resultat = self.updateInfoBank(infoBank,data)
        else:
            resultat = {'error':"veuiller completer d'abord les autres information"}       
        return resultat
        
    def updateInfoBank(self,infoBank,data):
        result = False
        print('ato------------------')
        print(infoBank,'update')
        # for e in infoBank:
        #     print(e.__meta)
        # try:
        #     for bankList in data:
        #         infoBank.bic = bankList['BIC']
        #         infoBank.iban = bankList['IBAN']
        #         infoBank.rib = bankList['RIB']
        #         infoBank.virement = bankList['virement']
        #         infoBank.plafond = bankList['plafond']
        #         infoBank.save()
        #         result = True
        # except Exception as e:
        #     print(e)

        return result