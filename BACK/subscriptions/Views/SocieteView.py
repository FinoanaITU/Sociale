from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, response
from subscriptions.Source.GestionSociete import GestionSociete
import json

class SocieteView():
    @csrf_exempt
    def allSociete(request):
        allSociete = GestionSociete().getAllSociete()
        jsonData = json.dumps(allSociete)
        print(type(jsonData))
        return JsonResponse(jsonData,safe=False)
