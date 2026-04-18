from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome
    
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.nome} - {self.especialidade}'
    
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('agendada', 'Agendada'),
            ('realizada', 'Realizada'),
            ('cancelada', 'Cancelada'),
        ],
        default='agendada'
    )
    
    def __str__(self):
        return f'{self.paciente} - {self.medico} - {self.data}'
