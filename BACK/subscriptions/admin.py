from django.contrib import admin
from . models import Posts, Utilisateur
from .Models import BulettinModel

admin.site.register(Posts)
admin.site.register(Utilisateur)
admin.site.register(BulettinModel.Motifs)
admin.site.register(BulettinModel.BulletinModel)