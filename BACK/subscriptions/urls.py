from django.urls import path
from . views import PostView
from .Views.SalarieView import SalarieView
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
    path('gestion-salarie/all-Salarie', SalarieView.allSalarieAction, name='get_all_Salarie')
]