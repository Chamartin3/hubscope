from django.contrib.auth.models import BaseUserManager ## A new class is imported. ##
from django.utils.translation import ugettext_lazy as _
# from  hubscope.persons.models import Profile
import uuid

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        """Create and save a User with the given email and password."""
        # if not email:
        #     raise ValueError('The given email must be set')
        # email = self.normalize_email(email)
        user = self.model(**extra_fields)
        # import pdb; pdb.set_trace()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if password is None:
            password='123456789'
        user = self._create_user(password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(password, **extra_fields)
        return user
