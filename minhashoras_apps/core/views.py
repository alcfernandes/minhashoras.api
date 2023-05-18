from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserAccountFilterMixin:
    """
    Mixin to filter queryset by the account of the logged user.

    Note: When using this mixin with other ViewSet classes, be sure to list
    this mixin before other classes to ensure the correct behavior.
    For example:

    class MyViewSet(UserAccountFilterMixin, ArchivableModelViewSet):
        pass
    """

    def get_queryset(self):
        super_viewset = super()
        if not hasattr(super_viewset, 'get_queryset'):
            raise TypeError(
                'UserAccountFilterMixin must be used with a ViewSet that has a get_queryset method.'
            )
        queryset = super_viewset.get_queryset()
        return queryset.filter(account__uuid=self.request.user.account.uuid)


class ArchivableModelViewSet(viewsets.ModelViewSet):
    show_archived_param = 'show-archived'

    def get_manager(self):
        if self.action == 'list':
            show_archived = self.request.query_params.get(
                self.show_archived_param
            )
            if not show_archived or show_archived.lower() == 'false':
                return self.queryset.model.active_objects
        return self.queryset.model.objects

    def get_queryset(self):
        manager = self.get_manager()
        return manager

    def already_archived_response(self):
        return Response(
            {'detail': _('This resource is already archived.')},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def already_unarchived_response(self):
        return Response(
            {'detail': _('This resource is not archived.')},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        request=None,  # It's not necessary to send a request body
    )
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        instance = self.get_object()
        if not instance.is_active:
            return self.already_archived_response()
        instance.archive()
        return Response(
            self.get_serializer(instance).data, status=status.HTTP_200_OK
        )

    @extend_schema(
        request=None,  # It's not necessary to send a request body
    )
    @action(detail=True, methods=['post'])
    def unarchive(self, request, pk=None):
        instance = self.get_object()
        if instance.is_active:
            return self.already_unarchived_response()
        instance.unarchive()
        return Response(
            self.get_serializer(instance).data, status=status.HTTP_200_OK
        )
