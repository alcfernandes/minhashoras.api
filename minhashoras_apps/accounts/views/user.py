from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.queryset
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=['GET'])
    def me(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)