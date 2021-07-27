from django.core.exceptions import MultipleObjectsReturned
from django.db.models.base import Model
from ..Models.BulettinModel import BulletinModel
from ..Models.BulettinModel import Motifs
from ..Models.BulettinModel import ModelMotif
from ..Models.SalarieModel import Societe

class GestionModel:
    def __init__(self, idSociete):
        self.societe = Societe.objects.get(id=idSociete)
        self.societeModel = BulletinModel.objects.filter(societe_id = idSociete)
        self._defaultModel = BulletinModel.objects.get(nom_model='Default')

    def trieMotifs (self,listMotif,initiale = True,model=''):
        data = []
        for motif in listMotif:
            categorie = ''
            if motif.isHeure == True:
                categorie = 'Heure'
            elif motif.isAbsence == True:
                categorie = 'Absence'
            elif motif.isPrime == True:
                categorie = 'Prime'
            elif motif.isIndemniter == True:
                categorie = 'Indemniter'
            elif motif.isAutre == True:
                categorie = 'Autre'

            if initiale == False:
                try:
                    modelActif = model if type(model) is BulletinModel  else model[0]
                    liaisonModel = ModelMotif.objects.get(model = modelActif, motif = motif)
                    data.append({'libelle': motif.libelle_motif, 'type': categorie, 'id':motif.id, 'isHaut':liaisonModel.isHaut })
                except MultipleObjectsReturned as e:
                    print(motif)
            else:
                data.append({'libelle': motif.libelle_motif, 'type': categorie, 'id':motif.id})

        return data

    def getSocieteModel(self):
        data = []
        print(self.societeModel)
        if len(self.societeModel) >= 1:
            for model in self.societeModel:
                if model.nom_model != 'Default':
                    data.append({'nomModel': model.nom_model, 'id': model.id})
        else:
            print('ato')
            data.append({'nomModel': str(self._defaultModel), 'id': self._defaultModel.id})
        return data

    def selectModel(self, nomModel):
        result = []
        modelActif = self.societeModel.filter(nom_model = nomModel) if nomModel != 'Default' else self._defaultModel
        if modelActif:
            listMotif = modelActif.get().motifs.all() if nomModel != 'Default' else modelActif.motifs.all()
            result = self.trieMotifs(listMotif,initiale= False, model=modelActif)
        return result

    def allMotif(self):
        listMotif = Motifs.objects.all()
        return self.trieMotifs(listMotif)

    def addOrUpdateModel(self,nomModel,data):
        resultat = True
        model = BulletinModel.objects.get_or_create(nom_model = nomModel, societe = self.societe) if nomModel != 'Default' else BulletinModel.objects.get(nom_model = nomModel)
        useModel = model[0] if nomModel != 'Default' else model
        ModelMotif.objects.filter(model= useModel).delete()
        for obj in data:
            try:
                if obj['type'] == 'Absence':
                    motif = Motifs.objects.get_or_create(libelle_motif=obj['libelle'], isAbsence = True)               
                if obj['type'] == 'Prime':
                    motif = Motifs.objects.get_or_create(libelle_motif=obj['libelle'], isPrime = True)             
                if obj['type'] == 'Autre':
                    motif = Motifs.objects.get_or_create(libelle_motif=obj['libelle'], isAutre = True)               
                if obj['type'] == 'Heure':
                    motif = Motifs.objects.get_or_create(libelle_motif=obj['libelle'], isHeure = True)
                if obj['type'] == 'Indemniter':
                    motif = Motifs.objects.get_or_create(libelle_motif=obj['libelle'], isIndemniter = True)

                if obj['isHaut'] == True:
                    liaison = ModelMotif(model=useModel, motif=motif[0], isHaut = True)
                else:
                    liaison = ModelMotif(model=useModel, motif=motif[0], isBas = True)

                liaison.save()
            except Exception as e :
                print(e)
                resultat = False
        return resultat

    def removeModel (self, nomModel):
        result = True
        try:
            model = BulletinModel.objects.get(nom_model = nomModel, societe = self.societe)
            ModelMotif.objects.filter(model= model).delete()
            BulletinModel.objects.filter(nom_model = nomModel, societe = self.societe).delete()
        except Exception as e:
            print(e)
            result = False
        return result
        