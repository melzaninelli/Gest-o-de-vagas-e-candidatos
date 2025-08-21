# 📝 Sistema de Gestão de Vagas e Candidatos

Este projeto é um **sistema simples de gestão de vagas e candidatos**, desenvolvido com **Django** para fins de aprendizado e testes técnicos.  

Ele permite:  
✅ Cadastrar **Candidatos**  
✅ Registrar **Candidaturas**  
✅ Criar e gerenciar **Vagas**  
✅ Acessar e administrar tudo pelo **Django Admin**  
✅ Visualizar um **painel (dashboard)** com informações básicas  

---

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/) 3.x  
- [Django](https://www.djangoproject.com/) 5.x  
- SQLite (banco de dados padrão do Django)  

---

## ⚙️ Como rodar o projeto
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
👉 http://127.0.0.1:8000/admin/
 – Administração
👉 http://127.0.0.1:8000/dashboard/
 – Dashboard

 projeto/
│── candidatos/      # App para cadastro de candidatos e candidaturas
│── vagas/           # App para cadastro de vagas
│── projeto/         # Configurações principais do Django
│── db.sqlite3       # Banco de dados
│── manage.py        # Arquivo de gerenciamento do Django
└── requirements.txt # Dependências do projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
