from django.urls import path
from .views import paciente_views, funcionario_views

urlpatterns = [
    # Métodos Paciente
    path('cadastrar_paciente', paciente_views.cadastrar_paciente, name='cadastrar_paciente'),
    path('editar_paciente/<int:id>', paciente_views.editar_paciente, name='editar_paciente'),
    path('remover_paciente/<int:id>', paciente_views.remover_paciente, name='remover_paciente'),
    path('lista_pacientes', paciente_views.listar_pacientes, name='lista_pacientes'),
    path('lista_paciente/<int:id>', paciente_views.listar_paciente_id, name='lista_paciente_id'),
    # Métodos Funciário
    path('cadastrar_funcionario', funcionario_views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('lista_funcionarios', funcionario_views.listar_funcionarios, name='lista_funcionarios')
]