from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework_simplejwt.authentication import JWTAuthentication

from minhashoras_apps.core.views import (
    ArchivableModelViewSet,
    UserAccountFilterMixin,
)

from ..models import Client
from ..serializers import (
    ClientCreateUpdateSerializer,
    ClientListSerializer,
    ClientRetrieveSerializer,
)


class ClientsViewSet(UserAccountFilterMixin, ArchivableModelViewSet):
    """
    Clients of the logged user's account.
    """

    authentication_classes = [JWTAuthentication]
    serializer_class = ClientRetrieveSerializer
    queryset = Client.objects.none()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name')

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ClientCreateUpdateSerializer
        else:
            return ClientRetrieveSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user.account)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='show-archived',
                description='Flag to include archived records.',
                required=False,
                type=bool,
                location=OpenApiParameter.QUERY,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
