from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    idade = serializers.SerializerMethodField()

    def get_idade(self, obj) -> int:
        return obj.idade

    class Meta:
        model = Cliente
        exclude = ()
