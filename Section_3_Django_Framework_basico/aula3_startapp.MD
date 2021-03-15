# Criar uma aplicação base

$ django_admin startapp core

core/migrations -> Histórico das migrações do banco de dados</br>
core/admin.py -> Administração do site django.</br>
core/models.py -> é o arquivo onde serão criados os modelos de dados, classes que serão persistidas no DB ou no projeto</br>
core/tests.py -> criação de testes.</br>
core/views.py -> onde será criado as viwes (funções) para definir as visões.</br>
</br>
Cada aplicação criada, ir no arquivo settings.py e incluir o nome da aplicação criada na lista
INSTALLED_APPS. Nesse mesmo arquivo, adicionar na lista Templates, na chave dir, o local onde terá os templates.

