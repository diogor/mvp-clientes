from math import floor
from datetime import date
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = PhoneNumberField()

    def __str__(self):
        return self.nome

    @property
    def idade(self) -> int:
        return int(floor((date.today() - self.data_nascimento).days / 365.25))
