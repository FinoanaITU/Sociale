from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, response
from subscriptions.Source.GestionModel import GestionModel
import json

class BulletinVue():

    @csrf_exempt
    def listeModelBulletin(request):
        data = json.loads(request.body)
        gestion = GestionModel(data['idSociete'])
        response = gestion.getSocieteModel()
        print(response)
        return JsonResponse(response,safe=False)

    @csrf_exempt
    def selectModel(request):
        data = json.loads(request.body)
        gestion = GestionModel(data['idSociete'])
        response = gestion.selectModel(data['nomModel'])
        return JsonResponse(response,safe=False)

    @csrf_exempt
    def allMotif (request):
        data = json.loads(request.body)
        gestion = GestionModel(data['idSociete'])
        response = gestion.allMotif()
        return JsonResponse(response,safe=False)