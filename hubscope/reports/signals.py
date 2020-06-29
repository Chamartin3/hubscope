
from hubscope.accounts.models import User
from django.contrib.auth.model import Group
from .models import Position
from termcolor import cprint
from django.db.models.signals import  post_save

def changed_position(sender,**kwargs):
    # Crea un perfil si se crea un nuevo usuario
    position = kwargs['instance']
    user = position.person
    group = Group.objects.get(name=position.name)
    cprint('AQUI','white','on_read')
    import pdb; pdb.set_trace()
    user.groups.set([group])

post_save.connect(changed_position, sender=Position)