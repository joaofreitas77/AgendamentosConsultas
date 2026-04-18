from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView,
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView,
    ConsultaListView, ConsultaCreateView, ConsultaUpdateView, ConsultaDeleteView
)

urlpatterns = [
    path('', ConsultaListView.as_view(), name='consulta_list'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/novo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/excluir/', PacienteDeleteView.as_view(), name='paciente_delete'),

    path('medicos/', MedicoListView.as_view(), name='medico_list'),
    path('medicos/novo/', MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/excluir/', MedicoDeleteView.as_view(), name='medico_delete'),

    path('consultas/', ConsultaListView.as_view(), name='consulta_list'),
    path('consultas/nova/', ConsultaCreateView.as_view(), name='consulta_create'),
    path('consultas/<int:pk>/editar/', ConsultaUpdateView.as_view(), name='consulta_update'),
    path('consultas/<int:pk>/excluir/', ConsultaDeleteView.as_view(), name='consulta_delete'),
]