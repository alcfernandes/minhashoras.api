from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Client
from ..serializers import (
    ClientCreateUpdateSerializer,
    ClientListSerializer,
    ClientSerializer,
)


class ClientsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = ClientSerializer

    def get_queryset(self):
        """
        Este view deve retornar uma lista de todos os clients ativos
        para a account atualmente autenticada.
        """
        user = self.request.user
        return Client.active_objects.filter(account__uuid=user.account.uuid)

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ClientCreateUpdateSerializer
        else:
            return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user.account)
