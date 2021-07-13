from subscriptions.Models.SocieteModel import Societe

class GestionSociete():
    def __init__(self, *args):
       pass
    
    def getAllSociete (self):
        societes = []
        try:
            allSocietes = Societe.objects.all()
            for sc in allSocietes:
                societes.append(sc.getSociete())
        except Exception as e:
            print(e)
        return societes
