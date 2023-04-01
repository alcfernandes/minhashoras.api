from django.conf import settings
from django.urls import path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter, SimpleRouter

from minhashoras_apps import __api_version__


@api_view()
def api_version(request):
    return Response({'api_version': __api_version__})


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = 'api'
urlpatterns = router.urls
urlpatterns += [
    path('version', api_version)
]
