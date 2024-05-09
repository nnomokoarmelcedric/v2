from django.urls import path
from . import views

urlpatterns=[
            path('requetes/reception',views.index_reception, name='requetes-index-reception'),
            path('requetes/envoye',views.index_envoye, name='requetes-index-envoye'),
            path('requetes/brouillons',views.index_brouillons, name='requetes-index-brouillons'),
            path('requetes/corbeille',views.index_corbeille, name='requetes-index-corbeille'),
            path('get_enseignants_by_departement/', views.get_enseignants_by_departement, name='get_enseignants_by_departement'),
            path('soumettre_requete/',views.soumettre_requete, name='soumettre-requete'),
            path('index_statistique_directeur/',views.index_statistique_directeur, name='index_statistique_directeur'),
            path('index_requetes_departement/<int:pk>/',views. index_requetes_departement, name='index-requetes-departement'),

        
]