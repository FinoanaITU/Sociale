from ..Models.BulettinModel import BulletinModel
from ..Models.BulettinModel import Motifs
from ..Models.SalarieModel import Societe

class GestionModel:
    def __init__(self, idSociete):
        self.societe = Societe.objects.get(id=idSociete)
        self.societeModel = BulletinModel.objects.filter(societe_id = idSociete)
        self._defaultModel = BulletinModel.objects.get(id=1)

    def trieMotifs (self, listMotif):
        data = []
        for motif in listMotif:
            if motif.isHeure == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Heure', 'id':motif.id })
            elif motif.isAbsence == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Absence', 'id':motif.id})
            elif motif.isPrime == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Prime', 'id':motif.id})
            elif motif.isIndemniter == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Indemniter', 'id':motif.id})
            elif motif.isAutre == True:
                 data.append({'libelle': motif.libelle_motif, 'type': 'Autre', 'id':motif.id})
        return data

    def getSocieteModel(self):
        data = []
        print(self.societeModel)
        if len(self.societeModel) >= 1:
            for model in self.societeModel:
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
            result = self.trieMotifs(listMotif)
        return result

    def allMotif(self):
        listMotif = Motifs.objects.all()
        return self.trieMotifs(listMotif)

    def addOrUpdateModel(self,nomModel,data):
        resultat = True
        model = BulletinModel.objects.get_or_create(nom_model = nomModel, societe = self.societe)
        motifList = []
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
                motifList.append(motif[0])
            except Exception as e :
                print(e)
                resultat = False
        model[0].motifs.set(motifList)
        return resultat

    def removeModel (self, nomModel):
        result = True
        try:
            model = BulletinModel.objects.get(nom_model = nomModel, societe = self.societe)
            model.motifs.all().delete()
            model.delete()
        except Exception as e:
            print(e)
            result = False
        return result
        