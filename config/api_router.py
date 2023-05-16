from django.conf import settings
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response

from minhashoras_apps import __api_version__
from minhashoras_apps.accounts import urls as accounts_urls
from minhashoras_apps.projects import urls as projects_urls


@api_view()
def api_version(request):
    return Response({'api_version': __api_version__})


app_name = 'api'
urlpatterns = [
    path('accounts/', include(accounts_urls)),
    path('projects/', include(projects_urls)),
    path('version', api_version),
]
