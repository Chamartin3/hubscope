from django.apps import apps
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from  hubscope.mixins import DatatablesMixin
from  hubscope.accounts.models import User
from  hubscope.accounts.serializers import (
                                            UserSerializer,
                                            UserRegistrationSerializer,
                                            PasswordSerializer,
                                            UserStatusSerializer,
                                            GroupsSerializer)
from rest_framework.permissions import IsAdminUser, BasePermission, DjangoModelPermissions

from termcolor import cprint
ADMIN_GROUPS=['admin']

# USER_RELATED_MODELS:{
#     'all':[
#         {'app':'capjv.persons', 'model':'Profile'}
#     ],
#     'socio':[
#         {'app':'capjv.persons', 'model':'Socio'}
#     ]
# }

# def create_related_models(self, arg):
    # pass



class ProfileOwnerPermission(BasePermission):
    """
    profile owner
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user == obj;

from django.utils.translation import gettext as _

class UserRegistration(generics.CreateAPIView):
    """docstring for UserRegistration."""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError as e:
            cause=e.args[1]
            # "Duplicate entry 'PGeren' for key 'username'"
            cause=cause.replace('Duplicate entry','Dato duplicado:') \
                .replace('for key','en el campo') \
                .replace('username','Nombre de Usuario')
            return Response({'message':cause}, status=401)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class MyInfo(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            data = {'user':serializer.data}
        else:
            data = {'user':None}
        return Response(data)



class UserList(DatatablesMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['first_name', 'last_name', 'username']
    # permission_classes = [IsAdminUser, DjangoModelPermissions]

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class UserInformation(generics.RetrieveUpdateAPIView):
    """docstring for UserRegistration."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ProfileOwnerPermission]

class UserDelete(generics.DestroyAPIView):
    """docstring for UserRegistration."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ChangeGroup(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):  
        kwargs['partial'] = True
        user=self.get_object()
        gname=request.data.get('groupname')
        # import pdb; pdb.set_trace()
        group=Group.objects.get(name=gname)
        user.groups.set([group])
        return Response(data={'message':'Permisos Cambiados con éxito'}, status=200)


class ChangePassword(generics.UpdateAPIView):
    """Allows to change passwords."""
    queryset = User.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['password'])
        user.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(data={'message':'La contraseña fue cambiada con éxito'}, status=200)


class UserStatusPermisions(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserStatusSerializer

    def update(self, request, *args, **kwargs):
        partial = True
        user_groups=request.data.get['groups']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user=self.get_object()
        user.groups.clear()
        if user.is_active and user_groups:
            grupos=Group.objects.filter(name__in=user_groups)
            if grupos:
                grupos=grupos.get()
                user.groups.add(*grupos)
                if [g.name for g in grupos] in ADMIN_GROUPS:
                    user.is_staff=True
                related_models=USER_RELATED_MODELS.get(g.name, None)
                if related_models:
                    for g_app in related_models:
                        model = apps.get_model(g_app.get('app'), g_app.get('model'))
                        model.objects.create(user=user)


            return Response({"message": "Permisos de usuario cambiados"}, status=200)
        return Response({"message": "Usuario Bloqueado"}, status=200)


class Auth(APIView):

    def get(self, request,*args, **kwargs):
        """ Logout a traves de una petición Ajax"""
        logout(request)
        return Response({"message": "Sesion Cerrada"}, status=202)

    def post(self, request, *args, **kwargs):
        """ Login a traves de una petición Ajax"""
  
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'message':"Exito"}, status=202)
            else:
                return Response({'message':"Este Usuario se ecneuntra inactivo o bloqueado, contacte a un adminitrador para mas información"}, status=401)
        else:
            return Response({'message':"Combinación de usuario y contraseña incorrecto"}, status=401)
