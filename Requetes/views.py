from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Ecole,Requete,Service,Profile,Departement
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure


@login_required
def index_requetes_departement(request,pk):
    profile = Profile.objects.get(utilisateur=request.user)
    dep = Departement.objects.get(id=pk)
    requetes = Requete.objects.filter(departement=dep)
    requetes_envoye = Requete.objects.filter(expediteur=profile).count()
    requetes_recu = Requete.objects.filter(destinataire=profile).count()
    context = {
        'requetes':requetes,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,

         }
    return render(request,'index_requetes_departement.html',context)
    

@login_required
def index_reception(request,pk=None):
    profile = Profile.objects.get(utilisateur=request.user)
    requetes_envoye = Requete.objects.filter(expediteur=profile).count()
    requetes_recu = Requete.objects.filter(destinataire=profile).count()
    requetes_non_lu = Requete.objects.filter(destinataire=profile,lu=False).count()
    requetes = Requete.objects.filter(destinataire=profile)
    departements = Departement.objects.all()
    service = Service.objects.all()
    existe = False
   

    
    if request.method == 'POST':
        statut = request.POST.get('statut')
        ida = request.POST.get('id')
        requete_id = request.POST.get('requeteId')
        remarque = request.POST.get('remarque')
        if statut and ida:
            requete = Requete.objects.get(id=ida)
            requete.statut = statut
            requete.lu = False
            account_sid = "ACf61cbba1c19f4458ed0384207b78178c"
            auth_token = "aae08a6d297456a704681e485debd282"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=f"{requete.expediteur.utilisateur.email} le statut de votre requete avec pour objet {requete.type} adresse a l'enseignant {requete.destinataire.utilisateur.email} a pour nouveaux statut  "+requete.statut,
            
            from_="+13156698536",
            to="+237655216330"
        )
            requete.save()
            print(statut)
            
            context = {
        'requetes':requetes,
        'requete' :requete,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'existe':existe,
        'requetes_non_lu':requetes_non_lu }
        elif remarque and ida:
            requete = Requete.objects.get(id=ida)
            requete.remarque = remarque
            requete.lu = False
            account_sid = "ACf61cbba1c19f4458ed0384207b78178c"
            auth_token = "aae08a6d297456a704681e485debd282"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=f"{requete.expediteur.utilisateur.email} votre requete avec objet  objet {requete.type} adresse a l'enseignant {requete.destinataire.utilisateur.email} a obtenu une reponse",
            from_="+13156698536",
            to="+237655216330"
        )
            requete.save()
            print(statut)
            context = {
        'requetes':requetes,
        'requete' :requete,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'existe':existe,
        'requetes_non_lu':requetes_non_lu }
        else:
         
            requete = Requete.objects.get(id=requete_id)
            requete.lu = True
            requete.save()
            context = {
        'requetes':requetes,
        'requete' :requete,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'existe':existe,
        'requetes_non_lu':requetes_non_lu
     }
        
        
    else:
        
        context = {
        'requetes':requetes,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'requetes_non_lu':requetes_non_lu

         }
    return render(request,'index_reception.html',context)

def get_enseignants_by_departement(request,pk=None):
    departement_id = request.GET.get('departement_id')
    if departement_id:
         profiles = Profile.objects.filter(departements__id=departement_id,role="ENSEIGNANT")
         enseignants = [{'id': profile.id, 'nom': profile.utilisateur.last_name, 'prenom': profile.utilisateur.first_name} for profile in profiles]
         print(enseignants)
         return JsonResponse({'enseignants': enseignants})
    else:
        return JsonResponse({})


@login_required
def index_envoye(request,pk=None):
    profile = Profile.objects.get(utilisateur=request.user)
    requetes_envoye = Requete.objects.filter(expediteur=profile).count()
    requetes_recu = Requete.objects.filter(destinataire=profile).count()
    requetes_non_lu = Requete.objects.filter(destinataire=profile,lu=False).count()
    requetes = Requete.objects.filter(expediteur=profile)
    departements = Departement.objects.all()
    service = Service.objects.all()
    existe = False


    
    if request.method == 'POST':
        existe = True
        requete_id = request.POST['requeteId']
        requete = Requete.objects.get(id=requete_id)
        
        context = {
        'requetes':requetes,
        'requete' :requete,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'existe':existe,
        'requetes_non_lu':requetes_non_lu
        


     }
        print(requete)
        
    else:
        
        context = {
        'requetes':requetes,
        'requetes_envoye':requetes_envoye,
        'requetes_recu':requetes_recu,
        'departements' :departements,
        'services' :service,
        'existe':existe,
        'requetes_non_lu':requetes_non_lu



         }
    print(existe)
    
    return render(request,'index_envoye.html',context)



@login_required
def index_brouillons(request):
    departements = Departement.objects.all()

    context = {
         }
    return render(request,'index_brouillons.html',context)


@login_required
def index_corbeille(request):
    departements = Departement.objects.all()

    context = {
         }
    return render(request,'index_corbeille.html',context)

@login_required
def soumettre_requete(request):
    if request.method == "POST":
        type = request.POST['type']
        objet = request.POST['objet']
        remarque = request.POST['preciser']
        contenu = request.POST['contenu']
        service = request.POST['service']
        departement = request.POST.get('departement',None)
        expediteur = Profile.objects.get(utilisateur=request.user)
        destinataire_id = request.POST.get('destinataire')
        print(destinataire_id)
        if destinataire_id:
            try:
                destinataire = Profile.objects.get(id=destinataire_id)
                print(destinataire)
            except Profile.DoesNotExist:
                destinataire = None
        else:
            destinataire = None
        documents = request.FILES.get('documents')
        
        if service:
            service = Service.objects.get(id=service)
            destinataire = Profile.objects.get(services=service)
        else:
            service = None
        
        if departement:
            departement = Departement.objects.get(id=departement)
        else:
            departement = None
        
        data = Requete(type=type, objet=objet, contenu=contenu, service=service, departement=departement,expediteur=expediteur,destinataire=destinataire,documents=documents)
        account_sid = "ACf61cbba1c19f4458ed0384207b78178c"
        auth_token = "aae08a6d297456a704681e485debd282"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body=f"  {destinataire.utilisateur.email} vous avez recu une requete de l'etudiant {expediteur.utilisateur.email} du departement {departement} avec objet {type}",
        from_="+13156698536",
        to="+237655216330"
        )
        data.save()
        print(message.sid)

        messages.success(request,f'requete cree avec succes')
        return redirect('requetes-index-envoye')
    else:
        return redirect('requetes-index-envoye')
    
@login_required
def index_statistique_directeur(request):
    dep = Departement.objects.get(id=1)
    requetes_3il= Requete.objects.filter(departement=dep).count()
    departements = Departement.objects.all()
    departement1 = "3IL"  # Département à rechercher
    statut1 = "ACCEPTE"  # Statut à rechercher
    statut2 = "EN APPEL"  # Statut à rechercher
    statut3 = "REFUSE"  # Statut à rechercher
    statut4 = "CLOTURE"  # Statut à rechercher
    statut5 = "EN ATTENTE DE TRAITEMENT"  # Statut à rechercher
    statut6 = "EN COURS DE TRAITEMENT"  # Statut à rechercher
    statut7 = "EN ATTENTE DE COMPLEMENT D'INFORMATION"  # Statut à rechercher

    # Compter le nombre de requêtes pour le département et le statut donné
    nb_requetes_accepte_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut1).count()
    nb_requetes_appel_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut2).count()
    nb_requetes_refuse_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut3).count()
    nb_requetes_cloture_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut4).count()
    nb_requetes_AT_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut5).count()
    nb_requetes_CT_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut6).count()
    nb_requetes_ACI_3IL = Requete.objects.filter(departement__nom=departement1, statut=statut7).count()
    context = {
        'accepte_3IL':nb_requetes_accepte_3IL,
        'appel_3IL':nb_requetes_appel_3IL,
        'refuse_3IL':nb_requetes_refuse_3IL,
        'cloture_3IL':nb_requetes_cloture_3IL,
        'at_3IL':nb_requetes_AT_3IL,
        'ct_3IL':nb_requetes_CT_3IL,
        'aci_3IL':nb_requetes_ACI_3IL,
        'requetes_3il':requetes_3il
         }
    print(context)
    return render(request,'index_statistique_directeur.html',context)

