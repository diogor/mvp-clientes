import hashlib
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from twilio.rest import Client
from .utils import generate_token


def upload_directory_path(instance, filename):
    return '{}/{}/{}.{}'.format(
        instance.__class__.__name__.lower(),
        str(instance.id),
        hashlib.sha224(filename.encode()).hexdigest(),
        filename.split(".")[-1:]
    )


class MyUserManager(BaseUserManager):
    def create_user(self, telefone, nome, password=None):
        if not telefone:
            raise ValueError('Users must have a phone #')

        user = self.model(
            telefone=telefone,
            nome=nome
        )

        user.set_password(password)
        user.token = generate_token()
        user.save(using=self._db)
        user.send_confirmation_code()
        return user

    def create_superuser(self, nome, telefone, password):
        if not telefone:
            raise ValueError('Users must have a phone #')

        user = self.model(
            telefone=telefone,
            nome=nome,
            is_superuser=True
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Grupo(models.Model):
    nome = models.CharField(max_length=300)
    logo = models.ImageField(null=True, upload_to=upload_directory_path)
    criador = models.ForeignKey('Perfil', on_delete=models.SET_NULL, null=True)
    url = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Perfil(AbstractBaseUser, PermissionsMixin):
    telefone = PhoneNumberField(unique=True)
    nome = models.CharField(max_length=300)
    avatar = models.ImageField(null=True, upload_to=upload_directory_path)
    grupos = models.ManyToManyField(Grupo, blank=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'telefone'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        ordering = ['nome']

    def get_full_name(self):
        return self.nome or self.telefone

    def __str__(self):
        return f'{self.nome} - {self.telefone}'

    def send_confirmation_code(self):
        client = Client(settings.TW_SID, settings.TW_TOKEN)

        message = client.messages.create(
            to=str(self.telefone),
            from_=settings.PHONE_NUMBER,
            body=f'Cod: {self.token}'
        )
