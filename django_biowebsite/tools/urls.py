from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('seq-content/', views.seqcontent_view, name='seqcontent'),
    path('reverse-comp/', views.revcomp_view, name='revcomp'),
    path('random-dna/', views.randomdna_view, name='randomdna'),
    path('translation/', views.translation_view, name='translation'),
]