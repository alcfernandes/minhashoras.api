from rest_framework.routers import DefaultRouter

from .views import ClientsViewSet

app_name = 'projects'

router = DefaultRouter()
router.register('clients', ClientsViewSet, basename='clients')

urlpatterns = router.urls
