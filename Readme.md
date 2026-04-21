# Sistema de Agendamento de Consultas

Projeto desenvolvido com Django para gerenciamento de consultas médicas, permitindo o cadastro de pacientes, médicos e agendamentos, com controle de acesso e autenticação de usuários.

---

## Objetivo

O sistema tem como objetivo facilitar o agendamento e gerenciamento de consultas em um contexto de saúde, permitindo organizar atendimentos de forma prática e segura.

---

## Tecnologias Utilizadas

- Python
- Django (Class-Based Views)
- PostgreSQL
- HTML
- CSS (tema escuro)
- ORM do Django

---

## Arquitetura

O projeto segue o padrão **MVT (Model-View-Template)** do Django.

- **Model:** definição das entidades do sistema
- **View:** lógica de negócio utilizando CBVs
- **Template:** interface do usuário

---

## Models

O sistema possui 3 modelos principais:

### Paciente
- nome
- cpf
- telefone
- email

### Médico
- nome
- especialidade
- crm
- email

### Consulta
- paciente (ForeignKey)
- médico (ForeignKey)
- data
- hora
- status
- observações

---

## Relacionamentos

- Um paciente pode ter várias consultas
- Um médico pode atender várias consultas
- Cada consulta pertence a um paciente e um médico

---

## Funcionalidades

- Login e logout de usuários
- Controle de permissões
- CRUD completo de:
  - Consultas
  - Pacientes
  - Médicos
- Filtros por:
  - paciente
  - médico
  - status
- Ordenação de dados
- Paginação
- Interface em tema escuro

---

## Autenticação e Autorização

- Sistema de login/logout com Django
- Uso de:
  - `LoginRequiredMixin`
  - `PermissionRequiredMixin`
- Controle de acesso por permissões:
  - criar
  - editar
  - excluir

---

## Equipe

- João Pedro
- Pablo Haimar
- Samuel Leite
- Marco Antônio
