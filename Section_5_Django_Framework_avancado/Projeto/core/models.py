import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    created = models.DateField(_('Created'), auto_now_add=True)
    modified = models.DateField(_('Modified'), auto_now=True)
    active = models.BooleanField(_('Active?'), default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES=(
        ('lni-cog', _('Gear')),
        ('lni-stats-up', _('Graphic')),
        ('lni-users', _('Users')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Rocket'))
    )
    services = models.CharField(_('Services'), max_length=100)
    description = models.TextField(_('Description'), max_length=200)
    icon = models.CharField(_('Icon'), max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.services

class Role(Base):
    role = models.CharField(_('Role'), max_length=100)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return self.role

class Team(Base):
    name = models.CharField(_('Name'), max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField(
        _('Image'),
        upload_to=get_file_path,
        variations={
        'thumbnail': {"width":480, "height":480, "crop":True}
        })
    facebook = models.CharField('Facebook', max_length=100, default="#")
    twitter = models.CharField('Twitter', max_length=100, default="#")
    instagram = models.CharField('Instagram', max_length=100, default="#")

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
    
    def __str__(self):
        return self.name