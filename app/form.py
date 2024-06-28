
from django import forms
from django.contrib.auth import get_user_model

from django.forms import DateInput, SelectDateWidget, ModelForm

from django.contrib.auth.forms import UserCreationForm


class PositionForm(forms.Form):
    position = forms.CharField()
from django import forms
from .models import Competence, Entreprise, Etudiant, Prof, Promo, Stage, Tuteur, TypeStage, Acquerir

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = '__all__'

class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields ='__all__'
class PromoForm(forms.ModelForm):
    class Meta:
        model = Promo
        fields = '__all__'
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'
class TuteurForm(forms.ModelForm):
    class Meta:
        model = Tuteur
        fields = '__all__'
class TypeStageForm(forms.ModelForm):
    class Meta:
        model = TypeStage
        fields = '__all__'

class AcquerirForm(forms.ModelForm):
    class Meta:
        model = Acquerir
        fields = '__all__'
