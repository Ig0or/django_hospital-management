from django.urls import path
from .views import paciente_views

urlpatterns = [
    path('cadastrar_paciente', paciente_views.cadastrar_paciente, name='cadastrar_paciente'),
]