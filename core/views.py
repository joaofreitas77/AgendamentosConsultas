from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente, Medico, Consulta

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
#Crud de paciente
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'core/paciente_list.html'
    context_object_name = 'pacientes'
    paginate_by = 5

class PacienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'core.add_paciente'

class PacienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nome', 'cpf', 'telefone', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'core.change_paciente'

class PacienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('paciente_list')
    permission_required = 'core.delete_paciente'
    
#Crud de medico
class MedicoListView(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'core/medico_list.html'
    context_object_name = 'medicos'
    paginate_by = 5


class MedicoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Medico
    fields = ['nome', 'especialidade', 'crm', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medico_list')
    permission_required = 'core.add_medico'


class MedicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Medico
    fields = ['nome', 'especialidade', 'crm', 'email']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medico_list')
    permission_required = 'core.change_medico'


class MedicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Medico
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('medico_list')
    permission_required = 'core.delete_medico'
    
#Crud de consulta com filtro, ordenação e paginação
class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'core/consulta_list.html'
    context_object_name = 'consultas'
    paginate_by = 5

    def get_queryset(self):
        queryset = Consulta.objects.select_related('paciente', 'medico').all()

        paciente = self.request.GET.get('paciente')
        medico = self.request.GET.get('medico')
        status = self.request.GET.get('status')
        ordem = self.request.GET.get('ordem')

        if paciente:
            queryset = queryset.filter(paciente__nome__icontains=paciente)

        if medico:
            queryset = queryset.filter(medico__nome__icontains=medico)

        if status:
            queryset = queryset.filter(status=status)

        if ordem == 'data':
            queryset = queryset.order_by('data', 'hora')
        elif ordem == 'paciente':
            queryset = queryset.order_by('paciente__nome')
        elif ordem == 'medico':
            queryset = queryset.order_by('medico__nome')
        else:
            queryset = queryset.order_by('-data', '-hora')

        return queryset
    
class ConsultaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Consulta
    fields = ['paciente', 'medico', 'data', 'hora', 'observacoes', 'status']
    template_name = 'core/form.html'
    success_url = reverse_lazy('consulta_list')
    permission_required = 'core.add_consulta'
    
class ConsultaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Consulta
    fields = ['paciente', 'medico', 'data', 'hora', 'observacoes', 'status']
    template_name = 'core/form.html'
    success_url = reverse_lazy('consulta_list')
    permission_required = 'core.change_consulta'
    
class ConsultaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('consulta_list')
    permission_required = 'core.delete_consulta'