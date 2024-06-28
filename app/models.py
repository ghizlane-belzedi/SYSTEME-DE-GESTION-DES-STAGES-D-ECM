from django.db import models

class Prof(models.Model):
    id_prof =models.CharField(primary_key=True, max_length=20)

    Qualite_CHOICES = [
        ('Mme', 'Mme'),
        ('M', 'M'),
    ]
    qualite_prof = models.CharField(max_length=5 ,choices=Qualite_CHOICES)
    nom_prof = models.CharField(max_length=255)
    prenom_prof = models.CharField(max_length=255,blank=True, null=True)
    adresse_prof = models.TextField(blank=True, null=True)
    tel_prof_eco = models.CharField(max_length=20,blank=True, null=True)
    c_postal = models.CharField(max_length=20,blank=True, null=True)
    ville = models.CharField(max_length=255,blank=True, null=True)
    tel_prof_dom = models.CharField(max_length=20,blank=True, null=True)
    date_depart = models.DateField(blank=True, null=True)
    date_embauche = models.DateField(blank=True, null=True)
 
class Competence(models.Model):
    code_comp = models.CharField(primary_key=True,max_length=20)
    libelle_comp = models.CharField(max_length=255)
    desc_comp = models.TextField()
class TypeStage(models.Model):
    id_type_stage = models.BigAutoField(primary_key=True)
    nb_sem = models.IntegerField()



class Promo(models.Model):
    annee_promo = models.DateField(primary_key=True)
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE)
    nb_inscr = models.IntegerField(blank=True, null=True)
    nb_recus = models.IntegerField(blank=True, null=True)


class Entreprise(models.Model):
    id_entreprise = models.BigAutoField(primary_key=True)
    forme_juridique = models.CharField(max_length=255)
    raison_sociale = models.CharField(max_length=255)
    adresse_ent = models.TextField()
    tel_ent = models.CharField(max_length=10)
    c_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=255)
    fax = models.CharField(max_length=10)
    contact_nom = models.CharField(max_length=255)
    tel_contact = models.CharField(max_length=10)
   
class Tuteur(models.Model):
    id_tuteur = models.CharField(primary_key=True, max_length=10)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    Qualite_CHOICES = [
        ('Mme', 'Mme'),
        ('M', 'M'),
    ]

    qualite_t = models.CharField(max_length=5 ,choices=Qualite_CHOICES)
    nom_t = models.CharField(max_length=255)
    prenom_t = models.CharField(max_length=255)
    tel_t = models.CharField(max_length=10)
    
class Etudiant(models.Model):
    id_Etud =models.CharField(primary_key=True, max_length=20)
    n_et_promo = models.IntegerField()
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    
    Qualite_CHOICES = [
        ('Mme', 'Mme'),
        ('M', 'M'),
    ]
    qualite_etud = models.CharField(max_length=5, choices=Qualite_CHOICES)
    nom_etud = models.CharField(max_length=255)
    prenom_etud = models.CharField(max_length=255)
    adresse_etud = models.TextField()
    suite = models.CharField(max_length=255, blank=True, null=True)
    c_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=255)
    
    SEXE_CHOICES = [
        ('M', 'Femme'),
        ('H', 'Homme'),
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField()
    tel_etud = models.CharField(max_length=20)
    mention = models.CharField(max_length=255, blank=True, null=True)

class Stage(models.Model):
    n_stage = models.BigAutoField(primary_key=True)
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    n_et_promo = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE)
    tuteur = models.ForeignKey(Tuteur, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    id_type_stage = models.ForeignKey(TypeStage, on_delete=models.CASCADE)
    annee_stage = models.DateField()
    compte_rendu = models.TextField(blank=True, null=True)



class Acquerir(models.Model):
    id = models.BigAutoField(primary_key=True)
    niveau_exige = models.IntegerField()
    code_comp = models.ForeignKey(Competence, on_delete=models.CASCADE)
    id_type_stage = models.ForeignKey(TypeStage, on_delete=models.CASCADE)
  