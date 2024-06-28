from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   
    path('', views.dashboard, name='index'),
    path('logout/', views.logout_view, name='log_out'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),#################entreprise#######
    path('entreprises/', views.entreprises, name='entreprises'),
    path('entreprise/<int:pk>/', views.view_entreprise, name='view_entreprise'),
    path('entreprise/create/', views.create_entreprise, name='create_entreprise'),
    path('entreprise/<int:pk>/update/', views.update_entreprise, name='update_entreprise'),
    path('entreprise/<int:pk>/delete/', views.delete_entreprise, name='delete_entreprise'),
########etudiant#########""
    path('etudiants/', views.etudiants, name='etudiants'),
    path('etudiant/<int:pk>/', views.view_etudiant, name='view_etudiant'),
    path('etudiant/create/', views.create_etudiant, name='create_etudiant'),
    path('etudiant/<int:pk>/update/', views.update_etudiant, name='update_etudiant'),
    path('etudiant/<int:pk>/delete/', views.delete_etudiant, name='delete_etudiant'),
########prof#########""
    ########prof#########""
    path('profs/', views.profs, name='profs'),
    path('prof/<str:pk>/', views.view_prof, name='view_prof'),
    path('prof/create/', views.create_prof, name='create_prof'),
    path('prof/<str:pk>/update/', views.update_prof, name='update_prof'),
    path('prof/<str:pk>/delete/', views.delete_prof, name='delete_prof'),
########tuteur#########""
path('tuteurs/', views.tuteurs, name='tuteurs'),
path('tuteur/<str:pk>/', views.view_tuteur, name='view_tuteur'),
path('tuteur/create/', views.create_tuteur, name='create_tuteur'),
path('tuteur/<str:pk>/update/', views.update_tuteur, name='update_tuteur'),
path('tuteur/<str:pk>/delete/', views.delete_tuteur, name='delete_tuteur'),
###########Stage################
 path('stages/', views.stages, name='stages'),
    path('stage/<int:pk>/', views.view_stage, name='view_stage'),
    path('stage/create/', views.create_stage, name='create_stage'),
    path('stage/<int:pk>/update/', views.update_stage, name='update_stage'),
    path('stage/<int:pk>/delete/', views.delete_stage, name='delete_stage'),

     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

