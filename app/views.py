# stockManagement/views.py
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from datetime import date
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static 
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Entreprise, Etudiant, Prof, Promo, Stage, Tuteur, TypeStage
from .form import EntrepriseForm, EtudiantForm, ProfForm, PromoForm, StageForm, TuteurForm, TypeStageForm

import locale
from datetime import date
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, FileResponse
from docx.shared import Inches, Pt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .form import PositionForm

# Create your views here.
#@login_required
# Create your views here.
#@login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    msg = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_tuteur:
                return redirect('tuteurs')
            elif user.is_professeur:
                return redirect('profs')
            else:
                return redirect('admin')  # Rediriger vers la page d'administration appropriée
        else:
            msg = 'Nom d\'utilisateur ou mot de passe incorrect'

    return render(request, 'registration/login.html', {'msg': msg})

def dashboard(request):
    etudiant_count = Etudiant.objects.count()
    prof_count = Prof.objects.count()
    tuteur_count = Tuteur.objects.count()
    entreprise_count = Entreprise.objects.count()
    stage_count = Stage.objects.count()

    # Pass the count to the template context
    context = {
        'etudiant_count': etudiant_count,
        'prof_count': prof_count, 
        'tuteur_count': tuteur_count,
        'entreprise_count': entreprise_count,
        'stage_count': stage_count, 
              }
    
    return render(request,'layout/dashboard.html',context)

def index(request):
    return render(request, 'layout/index.html')


#########"Entreprise################

def entreprises(request):
    entreprises = Entreprise.objects.all()
    return render(request, 'pages/entreprises.html', {'entreprises': entreprises})

def view_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    return render(request, 'pages/view_entreprise.html', {'entreprise': entreprise})

def create_entreprise(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entreprises')
    else:
        form = EntrepriseForm()
    return render(request, 'pages/create_entreprise.html', {'form': form})

def update_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('entreprises')
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'pages/create_entreprise.html', {'form': form})

def delete_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    entreprise.delete()
    return redirect('pages/entreprises')
###################Etudiant############

def etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'pages/etudiants.html', {'etudiants': etudiants})

def view_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    return render(request, 'pages/view_etudiant.html', {'etudiant': etudiant})

def create_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'pages/create_etudiant.html', {'form': form})

def update_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'pages/create_etudiant.html', {'form': form})

def delete_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    etudiant.delete()
    return redirect('etudiants')

###################Prof############

def profs(request):
    profs = Prof.objects.all()
    return render(request, 'pages/profs.html', {'profs': profs})


def create_prof(request):
    if request.method == 'POST':
        form = ProfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profs')
    else:
        form = ProfForm()
    return render(request, 'pages/create_prof.html', {'form': form})
def view_prof(request, pk):
    prof = get_object_or_404(Prof, pk=pk)
    return render(request, 'pages/view_prof.html', {'prof': prof})

def update_prof(request, pk):
    prof = get_object_or_404(Prof, pk=pk)
    if request.method == 'POST':
        form = ProfForm(request.POST, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('profs')
    else:
        form = ProfForm(instance=prof)
    return render(request, 'pages/create_prof.html', {'form': form})

def delete_prof(request, pk):
    prof = get_object_or_404(Prof, pk=pk)
    prof.delete()
    return redirect('profs')
##############tuteur#############
def tuteurs(request):
    tuteurs = Tuteur.objects.all()
    return render(request, 'pages/tuteurs.html', {'tuteurs': tuteurs})

def view_tuteur(request, pk):
    tuteur = get_object_or_404(Tuteur, pk=pk)
    return render(request, 'pages/view_tuteur.html', {'tuteur': tuteur})

def create_tuteur(request):
    if request.method == 'POST':
        form = TuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tuteurs')
    else:
        form = TuteurForm()
    return render(request, 'pages/create_tuteur.html', {'form': form})

def update_tuteur(request, pk):
    tuteur = get_object_or_404(Tuteur, pk=pk)
    if request.method == 'POST':
        form = TuteurForm(request.POST, instance=tuteur)
        if form.is_valid():
            form.save()
            return redirect('tuteurs')
    else:
        form = TuteurForm(instance=tuteur)
    return render(request, 'pages/create_tuteur.html', {'form': form})

def delete_tuteur(request, pk):
    tuteur = get_object_or_404(Tuteur, pk=pk)
    tuteur.delete()
    return redirect('tuteurs')


def stages(request):
    stages = Stage.objects.all()
    return render(request, 'pages/stages.html', {'stages': stages})

def view_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    return render(request, 'pages/view_stage.html', {'stage': stage})

def create_stage(request):
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stages')
    else:
        form = StageForm()
    return render(request, 'pages/create_stage.html', {'form': form})

def update_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    if request.method == 'POST':
        form = StageForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('stages')
    else:
        form = StageForm(instance=stage)
    return render(request, 'pages/create_stage.html', {'form': form})

def delete_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    stage.delete()
    return redirect('stages')