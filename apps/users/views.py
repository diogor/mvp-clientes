from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from .serializers import PerfilCreateSerializer, GrupoSerializer
from .models import Grupo


class ConfirmarTelefone(views.APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        numero = request.data.get('numero')
        codigo = request.data.get('codigo')
        if not numero or not codigo:
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            user = get_user_model().objects.get(telefone=numero)
        except get_user_model().DoesNotExist:
            return Response(
                {"numero": ["Usuário não encontrado."]},
                status=HTTP_400_BAD_REQUEST)
        if user.token != codigo.upper():
            return Response(
                {"codigo": ["Código não encontrado."]},
                status=HTTP_400_BAD_REQUEST
            )

        user.is_active = True
        user.token = None
        user.save()
        return Response(status=HTTP_202_ACCEPTED)


class PerfilViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = []
    serializer_class = PerfilCreateSerializer
    queryset = get_user_model().objects.filter(is_active=True)

    def perform_create(self, serializer):
        data = serializer.validated_data
        get_user_model().objects.create_user(
            data['telefone'], data['nome'], data['password']
        )


class GrupoViewSet(viewsets.ModelViewSet):
    serializer_class = GrupoSerializer
    queryset = Grupo.objects.filter(deleted=False)
