from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Grupo


class PerfilCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('telefone', 'password', 'nome')


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        exclude = ()
