# Entendendo o Django User Model

- Criar um pasta para o projeto ('Section_7_Djanto_User_Model\Projeto').
- Criar um projeto na pasta: `django-admin startproject django_user_model`
- Gerar o banco de dados: `python manage.py migrate`

No bash:

```python

>>> from django.contrib.auth.models import User

>>> from django.contrib.auth.models import User
>>> dir(User)
['DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', 
'_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_legacy_get_session_auth_hash', '_meta', '_password', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', 'check', 'check_password', 'clean', 'clean_fields', 'date_error_message', 'date_joined', 'delete', 'email', 'email_user', 'first_name', 'from_db', 'full_clean', 'get_all_permissions', 'get_deferred_fields', 'get_email_field_name', 'get_full_name', 'get_group_permissions', 'get_next_by_date_joined', 'get_previous_by_date_joined', 'get_session_auth_hash', 'get_short_name', 'get_user_permissions', 'get_username', 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'has_usable_password', 'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 'last_login', 'last_name', 'logentry_set', 'natural_key', 'normalize_username', 'objects', 'password', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'set_password', 'set_unusable_password', 'unique_error_message', 'user_permissions', 'username', 'username_validator', 'validate_unique']

>>> help(User)  
Help on class User in module django.contrib.auth.models:

class User(AbstractUser)
 |  User(*args, **kwargs)
 |
 |  Users within the Django authentication system are represented by this
 |  model.
 |
 |  Username and password are required. Other fields are optional.
 | [...]

>>> from django.contrib.auth.models import UserManager
>>> dir(UserManager)
['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_create_user', '_get_queryset_methods', '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 'create', 'create_superuser', 'create_user', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_by_natural_key', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'make_random_password', 'none', 'normalize_email', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list', 'with_perm']

```

Criando usuário:

```python
>>> usuario = User.objects.create_user(username='teste', password='123456', email='teste@gmail.com')
>>> usuario
<User: teste>
>>> usuario.save()

# Verificando no db existencia de usuarios
>>> ret = User.objects.all()
>>> ret
<QuerySet [<User: teste>]>
>>> ret[0]
<User: teste>
>>> ret[0].username
'teste'
>>> ret[0].email
'teste@gmail.com'
>>> ret[0].password
'pbkdf2_sha256$260000$jXbOgGweuyeQRQzcoskZfB$edtBHvcsqtjE9UenpXEHtg1gxr6R0qE4/FsSZ/jpQTs='

>>> ret[0].first_name

>>> user.first_name = 'Teste'
>>> user.last_name = 'otavio'
>>> user.save()

>>> ret1 = User.objects.get(id=1)
>>> ret1.first_name
'Teste'

>>> user.is_staff
False

# Ao tentar logar:

"""
Please enter the correct username and password for a staff account.
Note that both fields may be case-sensitive.
"""

>>> user.is_staff = True
>>> user.save()

```

Por padrão, os usuários criados nao fazem parte do staff, desse modo, não pode logar no django admin.
