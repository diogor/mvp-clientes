from rest_framework import viewsets
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiResponse,
)
from .models import Cliente
from .serializers import ClienteSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista de clientes",
        responses={
            200: OpenApiResponse(response=ClienteSerializer(many=True))
        },
    ),
    create=extend_schema(
        summary="Criar um cliente",
        request=ClienteSerializer,
        responses={201: OpenApiResponse(response=ClienteSerializer)},
    ),
)
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
