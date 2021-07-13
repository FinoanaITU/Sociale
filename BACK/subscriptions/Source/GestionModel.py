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
                data.append({'libelle': motif.libelle_motif, 'type': 'Heure'})
            elif motif.isAbsence == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Absence'})
            elif motif.isPrime == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Prime'})
            elif motif.isIndemniter == True:
                data.append({'libelle': motif.libelle_motif, 'type': 'Indemniter'})
            elif motif.isAutre == True:
                 data.append({'libelle': motif.libelle_motif, 'type': 'Autre'})
        return data

    def getSocieteModel(self):
        data = []
        print(self.societeModel)
        if len(self.societeModel) >= 1:
            for model in self.societeModel:
                data.append({'nomModel': model.nom_model})
        else:
            print('ato')
            data.append({'nomModel': str(self._defaultModel)})
        return data

    def selectModel(self, nomModel):
        modelActif = self.societeModel.filter(nom_model = nomModel) if nomModel != 'Default' else self._defaultModel
        listMotif = modelActif.get().motifs.all() if nomModel != 'Default' else modelActif.motifs.all()
        return self.trieMotifs(listMotif)

    def allMotif(self):
        listMotif = Motifs.objects.all()
        return self.trieMotifs(listMotif)
        