from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
    path('countries/<str:iso2>/', views.country_detail, name='country_detail'),
    path('p/<slug:slug>/', views.procedure_detail, name='procedure_detail'),
    path('documents/<int:document_id>/download/', views.sample_document_download, name='sample_document_download'),
]
