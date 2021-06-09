from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from subscriptions.Source.GestionSalarie import GestionSalarie
import json

class SalarieView():
    @csrf_exempt
    def identificationAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        response = gestion.ajoutIdentification(data['data'])
        return JsonResponse({"message":response})

    @csrf_exempt
    def coordonneeAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        response = gestion.ajoutCoordonnees(data['data'])
        print(response)
        return JsonResponse({"message":response})

    @csrf_exempt
    def emploiAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        response = gestion.ajoutEmploi(data['data'])
        print(response)
        return JsonResponse({"message":response})

    @csrf_exempt
    def infoBankAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        print(data)
        response = gestion.ajoutInfoBank(data['data'],data['idSalarie'])
        return JsonResponse({"message":response})

    @csrf_exempt
    def allInfoSalarieAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        response = gestion.recuperationAllInfoSalarie(data['data']['idSalarie'])
        return JsonResponse(response)

    @csrf_exempt
    def allSalarieAction(request):
        data = json.loads(request.body)
        gestion = GestionSalarie()
        response = gestion.getAllSalarie(data['idSociete'])
        print(type(response))
        jsonData = json.dumps(response)
        return JsonResponse(jsonData,safe=False)