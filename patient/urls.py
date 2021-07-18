
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.patient_list,name='list'),
    path('delete/<int:id>/', views.patient_delete, name='patient_delete'),
    path('<int:id>/', views.patient_ajouter,name='editer'),
    path('ajouter/',views.patient_ajouter,name='ajouter'),
    path('contact/',views.patient_contact,name='contact'),
]
