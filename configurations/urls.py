from django.urls import path
from . import views

app_name='configurations'

urlpatterns = [
    path('tableau/', views.tableau_de_bord, name='tableau'),
    path('conducteurs/', views.conducteur_list, name='conducteur_list'),
    path('conducteurs/search/', views.conducteur_search, name='conducteur_search'),
    path('conducteurs/edit/<int:pk>/', views.conducteur_edit, name='conducteur_edit'),    
]
