from rest_framework import status, viewsets
from rest_framework.response import Response


class ArchivableModelViewSet(viewsets.ModelViewSet):
    """
    This is an abstract ModelViewSet that overrides the default DELETE behavior
    to use a "soft delete" method called `archive`.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.archive()
        return Response(status=status.HTTP_204_NO_CONTENT)
