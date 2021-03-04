# Criar uma aplicação base

$ django_admin startapp core

core/migrations -> Historio das migrações do banco de dados
core/admin.py
core/models.py -> é o arquivo onde serão criados os modelos de dados, classes que serão persistidas no DB ou no projeto
core/tests.py -> criação de testes.
core/views.py

Cada aplicação criada, ir no arquivo settings.py e incluir o nome da aplicação criada na lista
INSTALLED_APPS. Nesse mesmo arquivo, adicionar na lista Templates, na chave dir, o local onde terá os templates.

