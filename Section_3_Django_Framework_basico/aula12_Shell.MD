# Shell Django

Para saber os comandos do manage.py, digite:
`python manage.py`

Para executar o shell:
`python manage.py shell`

```python

>>> from core.views import index
>>> dir(index)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', 
'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'] 

>>> produto = Produto (nome='atari 2600', preco=199.26, estoque=100)
>>> dir(Produto)

['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'estoque', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'nome', 'objects', 'pk', 'preco', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']

>>> from core.models import Cliente
>>> cliente = Cliente(nome='john', sobrenome='bobo', email='johnbobo@g.com')
>>> cliente.save()
>>> cliente.id
2

>>> cliente # chama o método wrapper
<Cliente: john>

>>> print(cliente) # chama o método __str__
john

>>> cliente.nome = 'ayusca'
>>> cliente.__dict__
{'_state': <django.db.models.base.ModelState object at 0x04132A00>, 'id': 2, 'nome': 'ayusca', 'sobrenome': 'bobo', 'email': 'johnbobo@g.com'}

>>> cliente.delete()
(1, {'core.Cliente': 1})

``` 