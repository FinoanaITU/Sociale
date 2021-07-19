from django.urls import path
from . views import PostView
from .Views.SalarieView import SalarieView
from .Views.SocieteView import SocieteView
from .Views.BulletinVue import BulletinVue
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('posts/', PostView.as_view(), name='posts_view'),
    path('gestion-salarie/ajout-identifiant', SalarieView.identificationAction, name='ajout_identification'),
    path('gestion-salarie/ajout-coordonee', SalarieView.coordonneeAction, name='ajout_coordoonee'),
    path('gestion-salarie/ajout-emploi', SalarieView.emploiAction, name='ajout_emploi'),
    path('gestion-salarie/ajout-infoBank', SalarieView.infoBankAction, name='ajout_infoBank'),
    path('gestion-salarie/all-infoSalarie', SalarieView.allInfoSalarieAction, name='get_all_infoSalarie'),
    path('gestion-salarie/all-Salarie', SalarieView.allSalarieAction, name='get_all_Salarie'),
    path('gestion-societ/all-Societe', SocieteView.allSociete, name='get_all_Societe'),

    ##Bulletin
    path('bulletin/liste-model', BulletinVue.listeModelBulletin, name='get_liste_model_bulletin'),
    path('bulletin/select-model', BulletinVue.selectModel, name='select_model_bulletin'),
    path('bulletin/all-motifs', BulletinVue.allMotif, name='all_motif'),
    path('bulletin/add-modif-model', BulletinVue.addOrModifModel, name='add_modif_model'),
    path('bulletin/remove-model', BulletinVue.removeModel, name='remove_model'),
]