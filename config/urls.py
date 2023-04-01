from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API base url
    path("api/", include("config.api_router")),
]
