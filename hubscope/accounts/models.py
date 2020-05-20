from django.db import models
from django.contrib.auth.models import AbstractUser
# from  hubscope.persons.models import Profile, Socio
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import class_prepared

from   hubscope.accounts.managers import UserManager

# def longer_username(sender, *args, **kwargs):
#     # You can't just do `if sender == django.contrib.auth.models.User`
#     # because you would have to import the model
#     # You have to test using __name__ and __module__
#     if sender.__name__ == "User" and sender.__module__ == "django.contrib.auth.models":
#         sender._meta.get_field("first_name").max_length = 75

# class_prepared.connect(longer_username)
# Create your models here.

class User(AbstractUser):
    """User model."""
    objects = UserManager()
    first_name = models.CharField(_('last name'), max_length=200, blank=True)
    last_name = models.CharField(_('first name'), max_length=200, blank=True)
    # date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ( {self.username})'
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        is_socio=len([g for g in self.groups.all() if g.name=="socio"])>0

        # prof, pcreated=Profile.objects.get_or_create(user=self)
        # if pcreated:
        #     print(f'Perfil creado para {self.fullname}')

        # if is_socio:
        #     socioprof, spcreated=Socio.objects.get_or_create(user=self, profile=self.profile)
        #     if spcreated:
        #         print(f'Perfil de socio creado con cedula {self.profile.cedula}')
        # prof, pcreated=Profile.objects.get_or_create(user=self)
        # if pcreated:
        #     print('Perfil creado')
        # print (self.id)
        # print (self)
        return self
