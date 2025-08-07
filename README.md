# Social Python - RedeSocial

desenvolvido com Django, focado em aprendizado, arquitetura de redes sociais, autenticação e deploy na Railway.

![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![Railway](https://img.shields.io/badge/Deploy-Railway-blue?logo=railway)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## ✨ Funcionalidades

- Autenticação de usuários (login, logout, cadastro)
- Postagem de tweets (limitado a 280 caracteres)
- Feed global e pessoal
- Perfil de usuário com foto
- Seguir e deixar de seguir usuários
- Listagem de seguidores e seguidos
- Curtir e retweetar publicações
- Upload de fotos de perfil
- Deploy pronto para produção

---

## 🛠️ Stack e Principais Tecnologias

- **Back-end:** Django 5
- **Banco de Dados:** SQLite (local) e PostgreSQL (produção Railway)
- **Frontend:** Django Templates (Bootstrap 4), Crispy Forms
- **Autenticação:** Django Allauth
- **Admin:** Django Admin
- **Outros:** Railway, Python 3.12

### Bibliotecas Utilizadas

- [`django-allauth`](https://github.com/pennersr/django-allauth) — Autenticação e login social
- [`crispy-forms`](https://github.com/django-crispy-forms/django-crispy-forms) — Estilização de formulários com Bootstrap 4
- [`widget-tweaks`](https://github.com/jazzband/django-widget-tweaks) — Customização dos campos de formulário no template
- [`dj-database-url`](https://github.com/jacobian/dj-database-url) — Configuração dinâmica de banco de dados (Railway)
- [`python-dotenv`](https://github.com/theskumar/python-dotenv) — Variáveis de ambiente

---

## 🔒 Segurança

- **Proteção CSRF**: Habilitada por padrão (middleware)
- **Validação de senha**: Regras nativas do Django (comprimento mínimo, senhas comuns, etc.)
- **Armazenamento seguro da SECRET_KEY**: Use variáveis de ambiente no deploy (nunca expor a chave secreta em produção)
- **Permissões**: Acesso às views controlado por decorators `@login_required`
- **Upload de mídia**: Pasta protegida, controle de acesso no código

---

## 🚀 Deploy

O projeto está pronto para deploy na [Railway](https://railway.app/), utilizando variáveis de ambiente para configurar o banco e a chave secreta. Basta criar o projeto na Railway, subir seu código e setar as variáveis:

- `DATABASE_URL`
- `SECRET_KEY`
- `DEBUG=false`

O projeto detecta automaticamente o ambiente (Railway ou local).

---


## ▶️ Como Rodar Localmente

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/social-python.git
cd social-python

# (Recom.) Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser

# Rode o servidor de desenvolvimento
python manage.py runserver

# Acesse em http://127.0.0.1:8000
models.py: Modelos do banco (Tweet, Follow, Like, Retweet, Usuario)

views.py: Lógicas das views e regras de negócio

forms.py: Formulários customizados para Tweet

urls.py: Rotas principais do app e da aplicação

settings.py: Configurações gerais do projeto

---


## Verifique todas as bibliotecas usadas em requirements.txt:
Django>=5.0
django-allauth
dj-database-url
python-dotenv
django-crispy-forms
crispy-bootstrap4
django-widget-tweaks
