# Definindo os models

Em Section_5_Django_Framework_avancado\Projeto\core\models.py:

```python
import uuid

from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    """
    Essa função vai gerar nomes aleatórios para o arquivo.
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField("Active?", default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES=(
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket')
    )
    services = models.CharField('Services', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.services

class Role(Base):
    role = models.CharField('Role', max_length=100)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role

class Team(Base):
    name = models.CharField('Name', max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField(
        'Image',
        upload_to=get_file_path,
        variations={
        'thumbnail': {"width":480, "height":480, "crop":True}
        })
    facebook = models.CharField('Facebook', max_length=100, default="#")
    twitter = models.CharField('Twitter', max_length=100, default="#")
    instagram = models.CharField('Instagram', max_length=100, default="#")

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
```

- No bash:

```bash

python manage.py makemigrations
python manage.py migrate

```

- Em Section_5_Django_Framework_avancado\Projeto\core\admin.py:

```python
from django.contrib import admin

from .models import Role, Service, Team
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('services', 'icon', 'active', 'modified')
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'modified')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'active', 'modified')

```
