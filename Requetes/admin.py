from django.contrib import admin

# Register your models here.
from .models import Profile,Universite,Ecole,Departement,Service,Requete
# Register your models here.

admin.site.register(Profile)
admin.site.register(Universite)
admin.site.register(Ecole)
admin.site.register(Departement)
admin.site.register(Service)
admin.site.register(Requete)

