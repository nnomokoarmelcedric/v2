from django.db import models
from enum import Enum
from django.utils import timezone
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.

class Universite(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    class Meta:
        db_table="Universite"

    def __str__(self):
        return self.nom

class Ecole(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE)
   
    class Meta:
        db_table = "Ecole"

    def __str__(self):
        return self.nom
     
class Departement(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)

    class Meta:
        db_table = "Departement"

    def __str__(self):
        return self.nom
    
class Service(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    universite = models.ForeignKey(Universite, on_delete=models.CASCADE, related_name='services')

    class Meta:
        db_table = "Service"

    def __str__(self):
        return self.nom
    

SEXE =(
    ('HOMME','HOMME'),
    ('FEMME','FEMME'),
    
)
APTITUDE =(
    ('APTE','APTE'),
    ('INAPTE','INAPTE'),
    
)
ROLE =(
    ('DIRECTEUR','DIRECTEUR'),
    ('CHEF DE DEPARTEMENT','CHEF DE DEPARTEMENT'),
    ('RESPONSABLE DE SERVICE','RESPONSABLE DE SERVICE'),
    ('ENSEIGNANT','ENSEIGNANT'),
    ('ETUDIANT','ETUDIANT'),
)
class Profile(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
    telephone = models.CharField(max_length=20)
    matricule = models.CharField(max_length=20)
    lieu_de_naissance = models.CharField(max_length=20)
    numero_CNI = models.CharField(max_length=20)
    aptitude =  models.CharField(max_length=20, choices=APTITUDE) 
    role =  models.CharField(max_length=40, choices=ROLE) 
    pays = CountryField()
    sexe = models.CharField(max_length=20, choices=SEXE)
    date_naissance = models.DateField(default = datetime.date(1990, 1, 1))
    image = models.ImageField(default='avatar.jpg',upload_to='Profile_Images')
    departements = models.ManyToManyField(Departement, blank=True)
    services = models.ManyToManyField(Service, blank=True)

    class Meta:
        db_table = "Profile"

    def __str__(self):
        return f'{self.utilisateur.username} '


TYPES =(
    ("DEMANDE DE DIPLOME","DEMANDE DE DIPLOME"),
    ("DEMANDE DE CORRECTION DE NOTE","DEMANDE DE CORRECTION DE NOTE"),
    ("DEMANDE DE TRANSFERT DE FILIERE","DEMANDE DE TRANSFERT DE FILIERE"),
    ("DEMANDE DE REEXAMEN","DEMANDE DE REEXAMEN"),
    ("DEMANDE D'ORIENTATION ACADEMIQUE","DEMANDE D'ORIENTATION ACADEMIQUE"),
    ("DEMANDE DE SOUTIENT PEDAGOGIQUE","DEMANDE DE SOUTIEN PEDAGOGIQUE"),
    ("DEMANDE D'UNE AUTORISATION D'ABSENCE","DEMANDE D'UNE AUTORISATION D'ABSENCE"),
    ("JUSTIFICATION D'ABSENCES","JUSTIFICATION D'ABSENCES"),
    ("AUTRES","AUTRES"),
)
STATUT =(

    ("EN ATTENTE DE TRAITEMENT","EN ATTENTE DE TRAITEMENT"),
    ("EN COURS DE TRAITEMENT","EN COURS DE TRAITEMENT"),
    ("EN ATTENTE DE COMPLEMENT D'INFORMATION","EN ATTENTE DE COMPLEMENT D'INFORMATION"),
    ("EN ATTENTE DE TRAITEMENT","EN ATTENTE DE TRAITEMENT"),
    ("ACCEPTE","ACCEPTE"),
    ("EN APPEL","EN APPEL"),
    ("REFUSE","REFUSE"),
    ("CLOTURE","CLOTURE"),





)
class Requete(models.Model):


    type =  models.CharField(max_length=40, choices=TYPES) 
    objet = models.CharField(max_length=200)
    contenu = models.TextField(max_length=2000)
    remarque = models.TextField(max_length=300, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    expediteur = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=False,related_name='expediteur_requetes')
    destinataire = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=False,related_name='destinataire_requetes')
    date_soumission = models.DateTimeField(auto_now_add=True)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    lu = models.BooleanField(default=False)
    statut = models.CharField(max_length=40, choices=STATUT,default="EN ATTENTE DE TRAITEMENT")

    
    class Meta:
        db_table = "Requete"
    def __str__(self):
        return f"La requete vient de Mr/Ms {self.expediteur.utilisateur.first_name}  {self.expediteur.utilisateur.last_name} a Mr/Ms{self.destinataire.utilisateur.first_name}  {self.destinataire.utilisateur.last_name}"

